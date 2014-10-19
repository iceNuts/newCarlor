# encoding: utf-8
#
# ChatGroup Model

import tornado
from tornado import gen
from mini import Document
from bson import ObjectId

class ChatGroup(Document):
    event_id        = str   #   associated event id (PUBLIC) / or nil as private
    in_party        = bool  #   True means special event 
    host_user_id    = str   #   host user id
    members         = list  #   user id list
    name            = str
    capacity        = int   #   default as 10 (UPGRADEABLE)
    photo_id        = str   #   ChatGroup description photo
    description     = str
    lottery         = bool  # if event needs lottery

    topic_arn       = str   # AWS topic arn 
    stored_topic_name = str # AWS stored topic name

    # make chatgroup subscribers
    @gen.coroutine
    def subscribers(self):
        users = collections.deque()
        subscribers = collections.deque()
        users.append(ObjectId(self.host_user_id))
        for uid in members:
            users.append(ObjectId(uid))
        cursor = self.db.APNs.find({'_id' : users})
        while(yield cursor.fetch_next):
            a = cursor.next_object()
            subscribers.append(
                {
                    'protocol' : 'application',
                    'endpoint' : a['aws_endpoint_arn']
                }
            )
        return subscribers
