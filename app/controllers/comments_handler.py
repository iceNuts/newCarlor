# encoding: utf-8

"""
class Comment

    key :from, String
    key :to, String
    key :content, String
    
    key :created_at, timestamp

end

"""

import tornado
from tornado import gen
from base_handler import BaseHandler
from utilities import param_filter
from bson import ObjectId
from datetime import datetime

__keys__ = {
    'from' : unicode,
    'to'   : unicode,
    'content' : unicode,
    'created_at' : datetime
}

class CommentsHandler(BaseHandler):

    # create a new comment 
    @gen.coroutine
    def post(self, uid=''):

        try:

            post_data = tornado.escape.json_decode(self.request.body)

            if not param_filter.is_ObjectID(uid):
                raise Exception('Invalid uid format')

            comment_from = uid
            comment_to = post_data['to']

            content = post_data['content']
            created_at = datetime.utcnow()

            yield self.db.comments.insert(
                {
                    'from' : comment_from,
                    'to'   : comment_to,
                    'content' : content,
                    'created_at' : created_at
                })

            self.write_json({'result' : 'OK'})

        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})

    # update a comment
    @gen.coroutine
    def put(self, uid='', comment_id=''):

        try:

            if not param_filter.is_ObjectID(uid) or not (yield db.users.find_one({'_id' : ObjectId(uid)})):
                raise Exception('Invalid uid format')

            comment = yield db.comments.find_one({'_id' : ObjectId(uid)})

            if not param_filter.is_ObjectID(comment_id) or not comment or not (str(comment['from']) == uid):
                raise Exception('Invalid comment id')            

            post_data = tornado.escape.json_decode(self.request.body)

            content = post_data['content']
            created_at = datetime.utcnow()

            yield self.comments.update(
                {'_id' : ObjectId(comment_id)},
                {'$set' : {'created_at' : created_at, 'content' : content}},
                )
            
            self.write_json({'result' : 'OK'})

        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})

    # delete a comment
    @gen.coroutine
    def delete(self, uid='', comment_id=''):

        try:

            if not param_filter.is_ObjectID(uid) or not (yield db.users.find_one({'_id' : ObjectId(uid)})):
                raise Exception('Invalid uid format')

            comment = yield db.comments.find_one({'_id' : ObjectId(uid)})

            if not param_filter.is_ObjectID(comment_id) or not comment or not (str(comment['from']) == uid):
                raise Exception('Invalid comment id')

            yield self.comments.remove({'_id' : ObjectId(comment_id)})

            self.write_json({'result' : 'OK'})

        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})

    # get user comment list
    def get(self, uid='', timestamp=''):

        try:

            if not param_filter.is_ObjectID(uid) or not (yield db.users.find_one({'_id' : ObjectId(uid)})):
                raise Exception('Invalid uid format')

            cursor = db.comments.find({'from' : ObjectId(uid), {'created_at' : {'$lt' : int(timestamp)}}})

            comments = yield cursor.to_list(length=20)

            self.write_json({'result' : comments})

        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})   


class CommentedHandler(BaseHandler):

    # get user's commented reviews
    def get(self, uid='', timestamp=''):

        try:

            if not param_filter.is_ObjectID(uid) or not (yield db.users.find_one({'_id' : ObjectId(uid)})):
                raise Exception('Invalid uid format')

            cursor = db.comments.find({'to' : ObjectId(uid), {'created_at' : {'$lt' : int(timestamp)}}})

            commenteds = yield cursor.to_list(length=10)

            self.write_json({'result' : commenteds})

        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})











