# encoding: utf-8

import tornado
import logging
import sys
import re
from tornado import gen
from utilities import my_json
from tornado.escape import json_encode

class BaseHandler(tornado.web.requestHandler):

    @property
    def db(self):
        return self.settings['db']

    @property
    def data(self):
        return tornado.escape.json_encode(self.request.body)

    def _handle_request_exception(self, e):
        err_msg = str(e)
        try:
            status_code = int(re.search(r'HTTP ([0-9]+):', err_msg).group(1))
            self.set_status(status_code)
        except Exception as foo:
            self.set_status(500)
        self.finish({'error' : err_msg})

    def write_json(self, data):
        data = self.clean_dict(data)
        self.write(json_encode(data))

    def clean_dict(self, data):
        return my_json.clean_bson(data)