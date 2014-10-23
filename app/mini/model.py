# encoding: utf-8
#
# Base Model


class DocMeta(type):

    def __new__(meta, name, bases, dict):
        def _check(self, attr, value):
            if attr in self.defaults:
                if not isinstance(value, self.defaults[attr]):
                    raise TypeError('%s cannot be %s' % (attr, value))
            else:
                raise TypeError('MongoDB document is frozen')

        def _setattr(self, attr, value):
            _check(self, attr, value)
            object.__setattr__(self, attr, value)

        cls = type.__new__(meta, name, bases, dict)
        # Set up default type for every attribute
        cls.defaults = {name: value for name, value in dict.items()}
        cls.__setattr__ = _setattr
        return cls


class Document(object):

    __metaclass__ = DocMeta

    # Convert to dict
    def to_dict(self):
        return self.__dict__

    # Convert to class
    def update(self, entries, options={}):
        clean_entries = self.firewall(entries, options)
        for key, value in clean_entries.items():
            # if isinstance(value, unicode):
            #         value = value.encode('utf-8')
            setattr(self, key, value)

    # delete attribute
    def delete(self, key):
        if key in self.__dict__:
            self.__dict__.pop(key)

    # Clear all stored values
    def clear(self):
        self.__dict__.clear()

    """ OVERRIDE this method to PROTECT document update """

    def firewall(self, dirty_entries, options={}):
        return dirty_entries
