from tornado import gen

from utilities.auth import get_user
from mini import BaseHandler


class AuthTokenHandler(BaseHandler):

    @gen.coroutine
    def post(self):
        user = yield self.current_user

        email = self.data['email']
        password = self.data['password']
        user = yield get_user(email, password)

        if not user:
            self.send_error(403)

        secret = self.settings['secret']

        token = user.create_token(secret)
        self.write_json({'token': str(token)})
