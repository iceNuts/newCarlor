# encoding: utf-8

import tornado
import logging
import sys
import re
import json
from exception import request_exception
from tornado import gen
from utilities import my_json
from tornado.escape import json_encode

class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.settings['db']

    @property
    def data(self):
        return json.loads(self.request.body)

    def _handle_request_exception(self, e):
        err_status, err_msg = request_exception(e)
        self.set_status(err_status)
        self.finish({'error' : err_msg})

    def write_json(self, data):
        data = self.clean_dict(data)
        self.set_header("Content-Type", "application/json")
        self.write(json_encode(data))

    def clean_dict(self, data):
        return my_json.clean_bson(data)