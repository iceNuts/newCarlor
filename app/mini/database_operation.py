# encoding: utf-8

import tornado
from tornado import gen
from mini import request_exception
from bson import ObjectId

# data should contain required fields only

@gen.coroutine
def post_doc(self, model, data):
    model.update(data, {'POST' : True})
    future = self.db[model.__class__.__name__].insert(model.to_dict())
    return future

# data should contain the object id

@gen.coroutine
def put_doc(self, model, data):
    object_id = data['_id']
    data.pop('_id')
    model.update(data, {'PUT' : True})
    future = self.db[model.__class__.__name__].update(
        {'_id' : ObjectId(object_id)},
        {'$set' : model.to_dict()})
    return future

# data should contain at least object id

@gen.coroutine
def get_doc(self, model, data):
    object_id = data['_id']
    doc = self.db[model.__class__.__name__].find_one({'_id' : ObjectId(object_id)})
    return doc

# data should contain at least object id

@gen.coroutine
def delete_doc(self, model, data):
    pass