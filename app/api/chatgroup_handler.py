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
        chatgroup = ChatGroup()
        yield aws.create_topic(self, chatgroup)
        yield post_doc(self, chatgroup, self.data)
        subscribers = yield chatgroup.subscribers(self)
        yield aws.subscribe_topic(self, chatgroup.topic_arn, subscribers)
        self.write_json({'result': 'OK'})

    # update a chatgroup information
    @gen.coroutine
    def put(self):
        yield put_doc(self, ChatGroup(), self.data)
        self.write_json({'result': 'OK'})

    # get chatgroup information
    @gen.coroutine
    def get(self, chatgroup_id=''):
        chatgroup_info = yield get_doc(self, ChatGroup(), {'_id': chatgroup_id})
        # need some filter later
        self.write_json({'result': chatgroup_info})

    # delete a chatgroup
    @gen.coroutine
    def delete(self, chatgroup_id=''):
        pass
