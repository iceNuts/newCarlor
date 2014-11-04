# encoding: utf-8

""" COMMON DEPENDENCIES """
from werkzeug.security import generate_password_hash

from tornado import gen
from mini import BaseHandler, async_login_required

""" COMMON DEPENDENCIES """

from models import User


class UserHandler(BaseHandler):
    # create a new user
    @gen.coroutine
    def post(self):
        data = self.data
        password = self.data['password']
        email = self.data['email'].strip()

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
        token = user.create_token()
        user_info = user.get_info()

        self.write_json({
            'token': token.decode('utf-8'),
            'user': user_info,
        })

    # update a user information
    @async_login_required
    @gen.coroutine
    def put(self):
        current_user = self.current_user
        yield current_user.save_info(self.data)

        self.write_json({'result': 'OK'})

    # get user information
    @async_login_required
    @gen.coroutine
    def get(self, uid=''):
        user = yield User.objects.get(uid)
        info = user.get_info()
        self.write_json({
            'user': info
        })
