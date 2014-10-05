"""
    Clean object_id in to_mongo dict

"""

import logging
from bson import ObjectId
from datetime import datetime


def clean_bson(input):
    try:
        output = input
        for key in input:
            if type(input[key]) == list:
                output[key] = clean_list(input[key])
            elif type(input[key]) == dict:
                output[key] = clean_dict(input[key])
            elif type(input[key]) == ObjectId or type(input[key]) == unicode:
                output[key] = str(input[key])
            elif type(input[key]) == datetime:
                output[key] = clean_strtime(input[key])
            else:
                output[key] = input[key]
        return output
    except Exception, e:
        logging.info(e)
        return output


def clean_list(input):

    output = []
    for val in input:
        if type(val) == ObjectId:
            output.append(str(val))
        else:
            output.append(val)

    return output

def clean_dict(input):

    output = {}
    for key in input:
        if type(input[key]) == ObjectId or type(input[key]) == unicode:
            output[key] = str(input[key])
        else:
            output[key] = input[key]
    return output

def clean_strtime(newdate):
    import time
    return time.mktime(newdate.timetuple())

    