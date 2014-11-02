from motorengine.fields.base_field import BaseField


class EnumField(BaseField):

    def __init__(self, options, *args, **kw):
        super(EnumField, self).__init__(*args, **kw)
        # options can only be list of int or str
        for i in options:
            if not (isinstance(i, int) or isinstance(i, str)):
                raise ValueError('the options of EnumField must be\
                                 list of string or integer')

        self.options = options

    def validate(self, value):
        return value is None or value in self.options


class PasswordField(BaseField):

    def validate(self, value):

        if len(value) < 6:
            return False
