# encoding: utf-8

import tornado
import json
from .exception import request_exception
from utilities import my_json
from tornado.escape import json_encode


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.settings['db']

    @property
    def sqs(self):
        return self.settings['sqs']

    @property
    def sns(self):
        return self.settings['sns']

    @property
    def data(self):
        return json.loads(self.request.body.decode('utf-8'))

    def _handle_request_exception(self, e):
        err_status, err_msg = request_exception(e)
        self.set_status(err_status)
        self.set_header("Content-Type", "application/json")
        self.finish({'error': err_msg})

    def write_json(self, data, is_clean=True):
        if not is_clean:
            data = self.clean_dict(data)

        self.set_header("Content-Type", "application/json")
        self.write(json_encode(data))

    def clean_dict(self, data):
        return my_json.clean_bson(data)
