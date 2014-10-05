import sys


class NetworkError(Exception):
    pass

class DataError(Exception):
    pass


# network exception decoration
def request_exception(fn):
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception, e:
            et, ev, tb = sys.exc_info()
            raise NetworkError, NetworkError(e), tb
    return wrapped

