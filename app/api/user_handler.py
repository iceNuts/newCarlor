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
        clean_data = User.firewall(self.data)
        new_user = User.from_son(clean_data)
        new_user.validate()
        yield new_user.save()
        self.write_json({'result' : 'OK'})

    # update a user information
    @gen.coroutine
    def put(self):
        clean_data = User.firewall(self.data)
        query = Q(_id=clean_data['_id'])
        users = yield User.objects.filter(query).find_all()
        right_user = users[0]
        for key, val in clean_data.items():
            right_user._values[key] = val
        right_user.validate()
        yield right_user.save()
        self.write_json({'result' : 'OK'})

    # get user information
    @gen.coroutine
    def get(self, uid='', options={}):
        entry = {'_id' : uid}
        clean_data = User.firewall(entry)
        query = Q(_id=clean_data['_id'])
        users = yield User.objects.filter(query).find_all()
        right_user = users[0]
        user_info = User.outputer(right_user.to_son(), options)
        self.write_json({'result' : user_info})

    # delete a user
    @gen.coroutine
    def delete(self, uid=''):
        entry = {'_id' : uid}
        clean_data = User.firewall(entry)
        query = Q(_id=clean_data['_id'])
        yield User.objects.filter(query).delete()
        self.write_json({'result' : 'OK'})
















