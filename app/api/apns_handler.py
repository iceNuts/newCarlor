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

from models import APNs
from mini import aws

class APNsHandler(BaseHandler):

    # create a new APNs and subscribe to AWS App
    @gen.coroutine
    def post(self):
        apns = APNs()
        yield aws.app_add_endpoint(self, apns)
        yield post_doc(self, apns, self.data)
        self.write_json({'result' : 'OK'})

    # delete APNs and unsubscribe to AWS App
    @gen.coroutine
    def delete(self):
        pass
