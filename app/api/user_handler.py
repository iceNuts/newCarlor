# encoding: utf-8

""" COMMON DEPENDENCIES """

import tornado
from tornado import gen
from mini import BaseHandler
from mini import request_exception
from mini import post_doc
from mini import put_doc
from mini import get_doc
from mini import delete_doc
from bson import ObjectId

""" COMMON DEPENDENCIES """

from models import User

class UserHandler(BaseHandler):

    # create a new user
    @request_exception
    def post(self):
        self.post_doc(User(), self.data)
        self.write_json({'result' : 'OK'})

    # update a user information
    @request_exception
    def put(self):
        self.put_doc(User(), self.data)
        self.write_json({'result' : 'OK'})

    # get user information
    @request_exception
    def get(self):
        user_info = self.get_doc(User(), self.data)
        # need some filter later
        self.write_json({'result' : user_info})

        
















