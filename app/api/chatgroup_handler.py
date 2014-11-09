# encoding: utf-8

""" COMMON DEPENDENCIES """

import tornado
from tornado import gen
from mini import BaseHandler
from mini import post_doc
from mini import put_doc
from mini import get_doc
from mini import delete_doc
from bson import ObjectId

""" COMMON DEPENDENCIES """

from models import ChatGroup
from mini import aws

class ChatgroupHandler(BaseHandler):

    # create a chatgroup
    @gen.coroutine
    def post(self):
        clean_data = ChatGroup.firewall(self.data)
        topic_data = yield aws.create_topic(clean_data['name'])
        clean_data['topic_arn'] = topic_data['topic_arn']
        clean_data['stored_topic_name'] = topic_data['stored_topic_name']
        new_chatgroup = ChatGroup.from_son(clean_data)
        new_chatgroup.validate()
        yield new_chatgroup.save()
        subscribers = yield new_chatgroup.subscribers(self)
        yield aws.subscribe_topic(self, chatgroup.topic_arn, subscribers)
        self.write_json({'result' : 'OK'})

    # update a chatgroup information
    @gen.coroutine
    def put(self):
        clean_data = ChatGroup.firewall(self.data)
        query = Q(_id=clean_data['_id'])
        chatgroups = yield ChatGroup.objects.filter(query).find_all()
        right_chatgroup = chatgroups[0]
        for key, val in clean_data.items():
            right_chatgroup._values[key] = val
        right_chatgroup.validate()
        yield right_chatgroup.save()
        self.write_json({'result' : 'OK'})

    # get chatgroup information
    @gen.coroutine
    def get(self, chatgroup_id='', options={}):
        entry = {'_id' : chatgroup_id}
        clean_data = ChatGroup.firewall(entry)
        query = Q(_id=clean_data['_id'])
        chatgroups = yield ChatGroup.objects.filter(query).find_all()
        right_chatgroup = chatgroups[0]
        chatgroup_info = ChatGroup.outputer(right_chatgroup.to_son(), options)
        # need some filter later
        self.write_json({'result' : chatgroup_info})

    # delete a chatgroup
    @gen.coroutine
    def delete(self, chatgroup_id=''):
        entry = {'_id' : uid}
        clean_data = ChatGroup.firewall(entry)
        query = Q(_id=clean_data['_id'])
        yield ChatGroup.objects.filter(query).delete()
        self.write_json({'result' : 'OK'})







