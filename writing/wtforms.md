---
title: Flask 下 wtforms 组件初始化
---

https://github.com/wtforms/wtforms/blob/master/wtforms/form.py


class ExperimentSetupForm(FlaskForm):
    reset = SubmitField('Reset')

    def __init__(self, setup_yaml, **form_kwargs):

        self.more_extra = self.meta.bind_field(
            self, TextAreaField(), options=extra_info_kwargs)
        self._fields['more_extra'] = self.more_extra
        self.process(**form_kwargs)


https://blog.csdn.net/qq_33733970/article/details/79027984

办法1:

https://stackoverflow.com/questions/43267820/how-to-bind-a-field-in-init-function-of-a-form

    self.field_3 = self._fields['field_3'] = self.meta.bind_field(
        self, TextAreaField(),
        {'name': 'field_3', 'prefix': self._prefix}
    )

process_data function of field object is not called automatically.

还要再加一个

    self.process(*kwargs)

class ExperimentSetupForm(FlaskForm):
    reset = SubmitField('Reset')

    def __init__(self, setup_yaml, **form_kwargs):

        self.more_extra = self.meta.bind_field(
            self, TextAreaField(), options=extra_info_kwargs)
        self._fields['more_extra'] = self.more_extra
        # run process
        self.process(**form_kwargs)



办法2:

https://stackoverflow.com/questions/31160781/wtforms-generate-fields-in-constructor

    class ExperimentSetupForm(FlaskForm):
        reset = SubmitField('Reset')

        def __init__(self, setup_yaml, **form_kwargs):

            # https://github.com/wtforms/wtforms/blob/3f955152b64a75b1d8cebf35bc9761a7216f4abd/wtforms/form.py#L193-L203
            
            # this will overwrite reset
            self._unbound_fields = OrderedDict()
            self._unbound_fields['submit'] = SubmitField('Submit')

            FlaskForm.__init__(self, **form_kwargs)



办法3:

http://wtforms.readthedocs.io/en/latest/fields.html#wtforms.fields.Field

> If `_form` and `_name` isn’t provided, an UnboundField will be returned instead. Call its bind() method with a form instance and a name to construct the field.

    class ExperimentSetupForm(FlaskForm):
        reset = SubmitField('Reset')

        def __init__(self, setup_yaml, **form_kwargs):

            FlaskForm.__init__(self, **form_kwargs)
            self._fields['submit'] = SubmitField('Save', _name='submit', _form=self)
            # not overwrite reset
