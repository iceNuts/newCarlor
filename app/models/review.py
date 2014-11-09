# encoding: utf-8
#
# Review Model

from motorengine import *
from datetime import datetime

class Review(Document):
    # must be special event
    event_id    = StringField(required=True)   
    # who wrote this
    user_id     = StringField(required=True)   
    time        = DateTimeField(auto_now_on_insert=True)
    detail      = StringField(required=True)
    title       = StringField(required=True)
