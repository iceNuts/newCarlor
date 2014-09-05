# encoding: utf-8

import tornado
from tornado import gen
from base_handler import BaseHandler

class IndexHandler(BaseHandler):

    @gen.coroutine
    def get(self):

        data = {
            'test' : 'yeah!'
        }

        yield self.db.messages.insert(
            {
                'user_id_a' : 'watashi',
                'user_id_b' : 'hontoni',
                'content'   : 'I love u'
            })
        
        data = yield self.db.messages.find_one({'user_id_a' : 'watashi'}, max_time_ms=100)
        self.write_json(data)