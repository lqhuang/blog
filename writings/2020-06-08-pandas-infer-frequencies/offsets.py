# https://github.com/pandas-dev/pandas/blob/master/pandas/_libs/tslibs/offsets.pyx

import re

opattern = re.compile(
    r"([+\-]?\d*|[+\-]?\d*\.\d*)\s*([A-Za-z]+([\-][\dA-Za-z\-]+)?)")

_lite_rule_alias = {
    "W": "W-SUN",
    "Q": "Q-DEC",
    "A": "A-DEC",  # YearEnd(month=12),
    "Y": "A-DEC",
    "AS": "AS-JAN",  # YearBegin(month=1),
    "YS": "AS-JAN",
    "BA": "BA-DEC",  # BYearEnd(month=12),
    "BY": "BA-DEC",
    "BAS": "BAS-JAN",  # BYearBegin(month=1),
    "BYS": "BAS-JAN",
    "Min": "T",
    "min": "T",
    "ms": "L",
    "us": "U",
    "ns": "N",
}

_dont_uppercase = {"MS", "ms"}

INVALID_FREQ_ERR_MSG = "Invalid frequency: {0}"

_offset_map = {}

prefix_mapping = {
    # offset._prefix: offset
    # for offset in [
    # YearBegin,  # 'AS'
    # YearEnd,  # 'A'
    # BYearBegin,  # 'BAS'
    # BYearEnd,  # 'BA'
    # BusinessDay,  # 'B'
    # BusinessMonthBegin,  # 'BMS'
    # BusinessMonthEnd,  # 'BM'
    # BQuarterEnd,  # 'BQ'
    # BQuarterBegin,  # 'BQS'
    # BusinessHour,  # 'BH'
    # CustomBusinessDay,  # 'C'
    # CustomBusinessMonthEnd,  # 'CBM'
    # CustomBusinessMonthBegin,  # 'CBMS'
    # CustomBusinessHour,  # 'CBH'
    # MonthEnd,  # 'M'
    # MonthBegin,  # 'MS'
    # Nano,  # 'N'
    # SemiMonthEnd,  # 'SM'
    # SemiMonthBegin,  # 'SMS'
    # Week,  # 'W'
    # Second,  # 'S'
    # Minute,  # 'T'
    # Micro,  # 'U'
    # QuarterEnd,  # 'Q'
    # QuarterBegin,  # 'QS'
    # Milli,  # 'L'
    # Hour,  # 'H'
    # Day,  # 'D'
    # WeekOfMonth,  # 'WOM'
    # FY5253,
    # FY5253Quarter,
    # ]
}


def _get_offset(name: str):  #-> BaseOffset:
    """
    Return DateOffset object associated with rule name.

    Examples
    --------
    _get_offset('EOM') --> BMonthEnd(1)
    """
    if name not in _dont_uppercase:
        name = name.upper()
        name = _lite_rule_alias.get(name, name)
        name = _lite_rule_alias.get(name.lower(), name)
    else:
        name = _lite_rule_alias.get(name, name)

    if name not in _offset_map:
        try:
            split = name.split("-")
            klass = prefix_mapping[split[0]]
            # handles case where there's no suffix (and will TypeError if too
            # many '-')
            offset = klass._from_name(*split[1:])
        except (ValueError, TypeError, KeyError) as err:
            # bad prefix or suffix
            raise ValueError(INVALID_FREQ_ERR_MSG.format(name)) from err
        # cache
        _offset_map[name] = offset

    return _offset_map[name]


def delta_to_tick(delta):  # -> Tick:
    if delta.microseconds == 0 and getattr(delta, "nanoseconds", 0) == 0:
        # nanoseconds only for pd.Timedelta
        if delta.seconds == 0:
            return Day(delta.days)
        else:
            seconds = delta.days * 86400 + delta.seconds
            if seconds % 3600 == 0:
                return Hour(seconds / 3600)
            elif seconds % 60 == 0:
                return Minute(seconds / 60)
            else:
                return Second(seconds)
    else:
        nanos = delta_to_nanoseconds(delta)
        if nanos % 1_000_000 == 0:
            return Milli(nanos // 1_000_000)
        elif nanos % 1000 == 0:
            return Micro(nanos // 1000)
        else:  # pragma: no cover
            return Nano(nanos)


def to_offset(freq):
    """
    Return DateOffset object from string or tuple representation
    or datetime.timedelta object.
    Parameters
    ----------
    freq : str, tuple, datetime.timedelta, DateOffset or None
    Returns
    -------
    DateOffset or None
    Raises
    ------
    ValueError
        If freq is an invalid frequency
    See Also
    --------
    DateOffset : Standard kind of date increment used for a date range.
    Examples
    --------
    >>> to_offset("5min")
    <5 * Minutes>
    >>> to_offset("1D1H")
    <25 * Hours>
    """

    delta = None
    stride_sign = None

    try:
        split = re.split(opattern, freq)
        if split[-1] != "" and not split[-1].isspace():
            # the last element must be blank
            raise ValueError("last element must be blank")

        print(split)

        tups = zip(split[0::4], split[1::4], split[2::4])
        # print(list(tups))

        for n, (sep, stride, name) in enumerate(tups):
            if sep != "" and not sep.isspace():
                raise ValueError("separator must be spaces")
            prefix = _lite_rule_alias.get(name) or name
            if stride_sign is None:
                stride_sign = -1 if stride.startswith("-") else 1
            if not stride:
                stride = 1

            if prefix in {"D", "H", "T", "S", "L", "U", "N"}:
                # For these prefixes, we have something like "3H" or
                #  "2.5T", so we can construct a Timedelta with the
                #  matching unit and get our offset from delta_to_tick
                td = Timedelta(1, unit=prefix)
                off = delta_to_tick(td)
                offset = off * float(stride)
                if n != 0:
                    # If n==0, then stride_sign is already incorporated
                    #  into the offset
                    offset *= stride_sign
            else:
                stride = int(stride)
                offset = _get_offset(name)
                offset = offset * int(np.fabs(stride) * stride_sign)

            if delta is None:
                delta = offset
            else:
                delta = delta + offset
    except (ValueError, TypeError) as err:
        raise ValueError(INVALID_FREQ_ERR_MSG.format(freq)) from err

    return delta


if __name__ == '__main__':
    to_offset("3D")
    to_offset("1D 2H")
    to_offset("1D2T")
    to_offset("D")
