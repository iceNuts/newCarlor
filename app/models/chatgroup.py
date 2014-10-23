# encoding: utf-8
#
# ChatGroup Model

import tornado
from tornado import gen
from mini import Document
from bson import ObjectId
import collections


class ChatGroup(Document):
    event_id = str  # associated event id (PUBLIC) / or nil as private
    in_party = bool  # True means special event
    host_user_id = str  # host user id
    members = list  # user id list
    name = str
    capacity = int  # default as 10 (UPGRADEABLE)
    photo = str  # ChatGroup description photo
    description = str
    lottery = bool  # if event needs lottery

    topic_arn = str   # AWS topic arn
    stored_topic_name = str  # AWS stored topic name

    # make chatgroup subscribers
    @gen.coroutine
    def subscribers(self, handler):
        users = []
        subscribers = []
        users.append(self.host_user_id)
        for uid in self.members:
            users.append(uid)
        cursor = handler.db.APNs.find({'user_id': {'$in': users}})
        while(yield cursor.fetch_next):
            a = cursor.next_object()
            subscribers.append(
                {
                    'protocol': 'application',
                    'endpoint': a['aws_endpoint_arn']
                }
            )
        return subscribers
