# encoding: utf-8
#
# ChatGroup Model

import tornado
from tornado import gen
from motorengine import *
from bson import ObjectId
import collections

class ChatGroup(Document):
    #   associated event id (PUBLIC) / or nil as private
    event_id        = StringField(required=True)  
    #   1 means special event  
    in_party        = IntField(required=True, min_value=0, max_value=1)  
    #   host user id
    host_user_id    = StringField(required=True)   
    #   user id list
    members         = ListField(StringField())  
    name            = StringField()
    #   default as 10 (UPGRADEABLE)
    capacity        = IntField(default=10)  
    #   ChatGroup description photo 
    photo_id        = StringField()   
    description     = StringField()
    # 1 if event needs lottery
    lottery         = IntField(min_value=0, max_value=1)   
    # AWS topic arn 
    topic_arn       = StringField(required=True) 
    # AWS stored topic name  
    stored_topic_name = StringField(required=True) 

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

    # make chatgroup subscribers
    @gen.coroutine
    def subscribers(self, handler):
        users = []
        subscribers = []
        users.append(self.host_user_id)
        for uid in self.members:
            users.append(uid)
        query = Q(user_id__in=users)
        result = yield APNs.objects.filter(query).find_all()
        for a in result:
            subscribers.append(
                {
                    'protocol' : 'application',
                    'endpoint' : a['aws_endpoint_arn']
                }
            )
        return subscribers
