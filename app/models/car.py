# encoding: utf-8
#
# Car Model

from motorengine import *

class Car(Document):
    user_id     = StringField(required=True)   #    user id
    brand       = StringField(required=True)
    color       = StringField(required=True)   #    hex string
    plate       = StringField(required=True)
    capacity    = IntField(required=True)
