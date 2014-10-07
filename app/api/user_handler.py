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

from models import User

class UserHandler(BaseHandler):

    # create a new user
    @gen.coroutine
    def post(self):
        yield post_doc(self, User(), self.data)
        self.write_json({'result' : 'OK'})

    # update a user information
    @gen.coroutine
    def put(self):
        yield put_doc(self, User(), self.data)
        self.write_json({'result' : 'OK'})

    # get user information
    @gen.coroutine
    def get(self, uid=''):
        user_info = yield get_doc(self, User(), {'_id':uid})
        # need some filter later
        self.write_json({'result' : user_info})


















