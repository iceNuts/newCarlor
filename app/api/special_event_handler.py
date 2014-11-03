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

from models import SpecialEvent
from mini import aws

class SpecialEventHandler(BaseHandler):

    # create a new special event
    @gen.coroutine
    def post(self):
        special_event = SpecialEvent()
        yield post_doc(self, special_event, self.data)
        self.write_json({'result' : event_list})

    # get special event list
    @gen.coroutine
    def get(self, option='future', timestamp=None, limit=20):
        event_list = []
        if option == 'future':
            event_list = yield SpecialEvent.get_future_event_with(self, timestamp, limit)
        self.write_json({'result' : event_list})