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


class MessageHandler(BaseHandler):

    # shoot a message to aws topic subscriber
    @gen.coroutine
    def post(self):
        yield aws.shoot_message(self)
        self.write_json({'result': 'OK'})
