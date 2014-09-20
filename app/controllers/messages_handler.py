# encoding: utf-8

"""

class

  key :message_type, image, voice, text
  key :message_content
  key :message_sender
  key :timestamp

end

"""


import tornado
import copy
from tornado import gen
from base_handler import BaseHandler
from utilities import param_filter
from utilities import aws_sns
from services import aws_sns
from bson import ObjectId
from datetime import datetime

__key__ = {
    'message_type' : unicode,
    'message_content' : unicode,
    'message_sender' : unicode,
}

class MesaagesHandler(BaseHandler):

    @gen.coroutine
    def post(self, chatgroup_id):

        try:
            if not param_filter.is_ObjectID(chatgroup_id):
                return Exception('Bad Chatgroup id Format')

            # grab sender info from session

            chatgroup = yield self.db.chatgroups.find_one({'_id' : ObjectId(chatgroup_id)})

            if not chatgroup:
                raise Exception('Chatgroup not exist')

            post_data = tornado.escape.json_decode(self.request.body)

            message_type = post_data['message_type']
            message_content = post_data['message_content']

            if not message_type in ['image', 'voice', 'text']:
                raise Exception('Bad message type')

            message = {
                'message_type' : message_type,
                'message_content' : message_content
            }

            aws_sns.apple(message_sender, message, chatgroup)

        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})



















