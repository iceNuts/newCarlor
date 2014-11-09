# encoding: utf-8
#
# UserEvent Model

from motorengine import *
from datetime import datetime

class UserEvent(Document):
    name            = StringField(required=True)
    #  user id
    host_user_id    = StringField(required=True)   
    detail          = StringField(required=True)
    #  2dsphere
    location        = JsonField()  
    start_time      = DateTimeField(required=True)
    end_time        = DateTimeField(required=True)
    photo_id        = StringField()
    capacity        = IntField(default=10)


