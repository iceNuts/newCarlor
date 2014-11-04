from tornado import gen
from mini import BaseHandler, async_login_required


class AuthTokenHandler(BaseHandler):

    @async_login_required
    @gen.coroutine
    def post(self):
        current_user = self.current_user

        token = current_user.create_token()
        self.write_json({'token': token.decode('utf-8')})
