# encoding: utf-8
#
# Like Model

from motorengine import *
from datetime import datetime
from bson import ObjectId

class Like(Document):
    # what you like
    liked_id        = StringField(required=True)
    # special or normal or comment
    event_type      = StringField(default='special', required=True)   
    # who does it
    uid             = StringField(required=True)