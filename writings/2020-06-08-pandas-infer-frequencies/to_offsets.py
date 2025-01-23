# Port from
# https://github.com/pandas-dev/pandas/blob/master/pandas/_libs/tslibs/offsets.pyx

import re
from datetime import timedelta
from typing import Callable, Dict, Union

opattern = re.compile(
    r"([+\-]?\d*|[+\-]?\d*\.\d*)\s*([A-Za-z]+([\-][\dA-Za-z\-]+)?)")

_lite_rule_alias = {
    "day": "D",
    "days": "D",
    "hour": "H",
    "hours": "H",
    "min": "T",
    "ms": "L",
    "us": "U",
    # "ns": "N",
}

_timedelta_args = {
    "D": "days",
    "H": "hours",
    "T": "minutes",
    "S": "seconds",
    "L": "milliseconds",
    "U": "microseconds",
}

INVALID_FREQ_ERR_MSG = "Invalid frequency: {0}"


class Timedelta(timedelta):
    def __int__(self):
        return int(self.total_seconds())

    def __float__(self):
        return self.total_seconds()

    def __str__(self) -> str:
        return str(self.total_seconds())


def to_timedelta(
        freq: str,
        Timedelta: Callable = timedelta) -> Union[timedelta, Timedelta]:
    """
    Return datetime.timedelta object from string or tuple representation

    Args:
        freq : str, tuple, datetime.timedelta

    Returns:
        timedelta or None

    Raises:
        ValueError: If freq is an invalid frequency

    Examples:
        >>> to_timedelta("5min")
        datetime.timedelta(seconds=300)
        >>> to_timedelta("1D1H")
        datetime.timedelta(days=1, seconds=3600)
    """

    delta_args: Dict[str, float] = {}

    try:
        split = re.split(opattern, freq)
        if split[-1] != "" and not split[-1].isspace():
            # the last element must be blank
            raise ValueError("last element must be blank")

        tups = zip(split[0::4], split[1::4], split[2::4])
        # print(split)
        # print(list(tups)) # list will make `tups` unuseable

        for n, (sep, stride, name) in enumerate(tups):
            if sep != "" and not sep.isspace():
                raise ValueError("separator must be spaces")
            prefix = _lite_rule_alias.get(name.lower()) or name
            stride_sign = -1 if stride.startswith("-") else 1
            if not stride:
                stride = 1  # type: ignore

            if prefix in {"D", "H", "T", "S", "L", "U"}:
                # For these prefixes, we have something like "3H" or
                #  "2.5T", so we can construct a timedelta with the
                #  matching unit
                delta_args[
                    _timedelta_args[prefix]] = stride_sign * float(stride)
            else:
                raise ValueError(f"Unkown time freq unit: {prefix}")

        delta = Timedelta(**delta_args)  # type: ignore

    except (ValueError, TypeError) as err:
        raise ValueError(INVALID_FREQ_ERR_MSG.format(freq)) from err

    return delta


def test_to_timedelta():
    a = to_timedelta("3D", Timedelta=timedelta)
    b = to_timedelta("1D 2H", Timedelta=timedelta)
    c = to_timedelta("1D2T", Timedelta=timedelta)
    d = to_timedelta("D", Timedelta=timedelta)

    assert str(a) == "3 days, 0:00:00"
    assert str(b) == "1 day, 2:00:00"
    assert str(c) == "1 day, 0:02:00"
    assert str(d) == "1 day, 0:00:00"

    assert a.total_seconds() == 3 * 24 * 3600
    assert b.total_seconds() == 1 * 24 * 3600 + 2 * 3600
    assert c.total_seconds() == 1 * 24 * 3600 + 2 * 60
    assert d.total_seconds() == 24 * 3600


def test_to_custom_timedelta():
    a = to_timedelta("3D")
    b = to_timedelta("1D 2H")
    c = to_timedelta("1D20L")
    d = to_timedelta("D")

    assert int(c) == 86400

    assert str(a) == "259200.0"
    assert str(b) == "93600"
    assert str(c) == "86400"
    assert str(d) == "86400"

    assert a.total_seconds() == 3 * 24 * 3600
    assert b.total_seconds() == 1 * 24 * 3600 + 2 * 3600
    assert c.total_seconds() == 1 * 24 * 3600 + 2 * 60
    assert d.total_seconds() == 24 * 3600


if __name__ == "__main__":

    to_timedelta("3D")
    to_timedelta("1D 2H 3T")
    to_timedelta("1D2T")
    to_timedelta("D")

    # to_timedelta("3D-1T")  # not work for now

    test_to_timedelta()
    test_to_custom_timedelta()
