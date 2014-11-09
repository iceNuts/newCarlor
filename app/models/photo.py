# encoding: utf-8
#
# Photo Model

from motorengine import *

class Photo(Document):
    #   associated object id
    object_id   = StringField(required=True)
    #   photo link
    s3_link     = URLField(required=True)   
