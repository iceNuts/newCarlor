# encoding: utf-8

"""

class
  
  key :users_list
  key :chat_group_name

end

"""
        

import tornado
from tornado import gen
from base_handler import BaseHandler
from utilities import param_filter
from bson import ObjectId

__keys__ = {
    'users_list' : list,
    'chat_group_name' : unicode,
}   
    
class ChatgroupsHandler(BaseHandler): 
    
    # create a chat group
    # @user_list @chat_group_name
    @gen.coroutine
    def post(self):

        try:
            post_data = tornado.escape.json_decode(self.request.body)
            users_list = post_data['users']
            chat_group_name = post_data['group_name']

            #param check
            if type(users_list) != __keys__['users_list'] 
            or type(chat_group_name) != __keys__['chat_group_name']:
                raise Exception('Invalid Format')

            for uid in users_list:
                if not (yield self.db.users.find_one({'_id' : ObjectId(uid)})):
                    raise Exception('The user not exist')

            yield self.db.chatgroups.insert({
                    'users_list' : users_list,
                    'chat_group_name' : chat_group_name
                })

            self.write_json({'result' : 'OK'})
        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})


    # update a chat group
    @gen.coroutine
    def put(self, chatgroup_id):

        try:
            if not param_filter.is_ObjectID(chatgroup_id):
                raise Exception('Bad chatgroup id Format')

            if not yield self.db.chatgroups.find_one({'_id' : ObjectId(chatgroup_id)}):
                raise Exception('Chatgroup not exist')

            post_data = tornado.escape.json_decode(self.request.body)
            users_list = post_data['users']
            chat_group_name = post_data['group_name']

            #param check
            if type(users_list) != __keys__['users_list'] 
            or type(chat_group_name) != __keys__['chat_group_name']:
                raise Exception('Invalid Format')

            for uid in users_list:
                if not (yield self.db.users.find_one({'_id' : ObjectId(uid)})):
                    raise Exception('The user not exist')

            yield self.db.chatgroups.update(
                {'_id' : ObjectId(chatgroup_id)},
                {'$set' : {
                    'users_list' : users_list,
                    'chat_group_name' : chat_group_name
                    }}
                )
            self.write_json({'result' : 'OK'}) 

        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})


    # get a chat group
    @gen.coroutine
    def get(self, chatgroup_id):

        try:
            if not param_filter.is_ObjectID(chatgroup_id):
                raise Exception('Bad chatgroup id Format')

            chatgroup_data = yield self.db.chatgroups.find_one({'_id' : ObjectId(chatgroup_id)})
            if not chatgroup_data:
                raise Exception('Chatgroup not exist')

            self.write_json({'result' : chatgroup_data})

        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})


    # delete a chat group
    @gen.coroutine
    def delete(self, chatgroup_id):

        try:

            if not param_filter.is_ObjectID(chatgroup_id) or not (yield db.chatgroups.find_one({'_id' : ObjectId(uid)})):
                raise Exception('Invalid uid format')

            yield self.chatgroups.remove({'_id' : ObjectId(chatgroup_id)})

            self.write_json({'result' : 'OK'})

        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})












