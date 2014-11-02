# encoding: utf-8

""" COMMON DEPENDENCIES """
from werkzeug.security import generate_password_hash

from tornado import gen
from mini import BaseHandler
from mini import put_doc
from mini import get_doc

""" COMMON DEPENDENCIES """

from models import User


class UserHandler(BaseHandler):

    # create a new user
    @gen.coroutine
    def post(self):
        data = self.data
        password = self.data['password']
        email = self.data['email']

        user = yield User.get_user_by_email(email)

        if user:
            self.write_json({
                'status': 0,
                'error': 'Email already in use'
            })
            return

        hashed_password = generate_password_hash(password)
        data['password'] = hashed_password

        user = User(**data)
        yield user.save()

        self.write_json(data)

    # update a user information
    @gen.coroutine
    def put(self):
        yield put_doc(self, User(), self.data)
        self.write_json({'result': 'OK'})

    # get user information
    @gen.coroutine
    def get(self, uid=''):
        self.write(uid)
        return
        user_info = yield get_doc(self, User(), {'_id': uid})
        # need some filter later
        self.write_json({'result': user_info})
