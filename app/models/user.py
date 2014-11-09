# encoding: utf-8
#
# User Model

from mini import Document
from datetime import datetime

class User(Document):
    first_name      = StringField(required=True)
    last_name       = StringField(required=True)
    birthday        = DateTimeField(required=True)
    email           = StringField(required=True)
    password        = StringField(required=True)
    phone           = StringField(required=True)
    school          = StringField(required=True)
    major           = StringField(required=True)
    # F femail / M male
    gender          = StringField(required=True, default='M')   
    signature       = StringField()
    driver          = IntField(default=0)
    email_active    = IntField(default=0)
    phone_active    = IntField(default=0)
    account_active  = IntField(default=0)
    driver_license  = StringField()
    # has_a car => Car
    car_id          = StringField()   
    # has_a profilephoto => Photo 
    photo_id        = StringField()   

    # OVERRIDE THIS TO PROTECT YOUR DATA
    # SET SOME DEFAULT VALUE
    # CHECK KEY NAME
    # CONVERT TO PROPER TYPE
    @classmethod
    def firewall(self, dirty_entries, options={}):
        
        return dirty_entries

    # FILTER OUT SOME SENSITIVE FIELDS
    @classmethod
    def outputer(self, incoming, options={}):

        return incoming