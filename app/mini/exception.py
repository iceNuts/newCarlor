import sys
import bson

# request exception decoration
# naive implementation


def request_exception(error):
    err_msg = str(error)
    try:
        err_status = 500
        if "bson" in str(type(error)):
            err_status = 400
        if "TypeError" in str(type(error)):
            err_status = 400
    except Exception as e:
        print(e)

    return err_status, err_msg
