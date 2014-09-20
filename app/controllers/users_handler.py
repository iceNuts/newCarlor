# encoding: utf-8

"""
class User
  
  key :first_name, String
  key :last_name, String
  key :email, String
  key :password, String
  key :phone, String
  key :nationality, String
  key :major, String
  key :gender, String
  key :car_brand, String
  key :car_color, String
  key :car_plate, String
  key :user_signature, String

  key :type, Integer # (0 Faculty/1 Student)

  key :driver_flag, Bool 

  key :email_verified, Bool
  key :phone_verified, Bool

  many :comments
  many :photos
  many :likes
  many :posts
  many :blockeds

end

"""

import tornado
from tornado import gen
from base_handler import BaseHandler
from utilities import param_filter
from bson import ObjectId

__keys__ = {
    'first_name' : unicode,
    'last_name' : unicode,
    'email' : unicode,
    'password' : unicode,
    'phone' : unicode,
    'nationality' : unicode,
    'major' : unicode,
    'gender' : unicode,
    'car_brand' : unicode,
    'car_color' : unicode,
    'car_plate' : unicode,
    'user_signature' : unicode,
    'type' : int,
    'driver_flag' : bool,
}

class UsersHandler(BaseHandler):    

    # create a new user
    # @password @email @identity required
    @gen.coroutine
    def post(self):

        try:
            post_data = tornado.escape.json_decode(self.request.body)
            email = post_data['email']
            password = post_data['password']

            # param check
            if (not param_filter.is_email(email)):
                raise Exception('input parameter error')
            elif (yield self.db.users.find_one({'email' : email})):
                raise Exception('email has been registered')

            yield self.db.users.insert(
                {
                    'email' : email,
                    'password' : password,
                })

            self.write_json({'result' : 'OK'})
        
        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})


    # update a user information
    # validate post body key arguments
    @gen.coroutine
    def put(self, uid=''):
        try:
            post_data = tornado.escape.json_decode(self.request.body)

            user_data = yield self.db.users.find_one({'_id' : ObjectId(uid)})

            if param_filter.is_ObjectID(uid) and user_data:

                for key, value in post_data.iteritems():
                    if (not key in __keys__.keys()) or (type(value) != __keys__[key]):
                        raise Exception('Bad ' + str(key) + ' Input')

                if post_data.has_key('email'):
                    raise Exception('Can not Contain Email')
                if post_data.has_key('type') and not post_data['type'] in [0, 1]:
                    raise Exception('Bad Type Value')
                if post_data.has_key('phone') and not param_filter.is_phone(post_data['phone']):
                    raise Exception('Bad Phone Number Format')

                yield self.db.users.update(
                    {'_id' : ObjectId(uid)},
                    {'$set' : post_data},
                    )
                self.write_json({'result' : 'OK'})    
            else:
                raise Exception('user not exist')
        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})


    # get user information
    @gen.coroutine
    def get(self, uid=''):

        try:

            if not param_filter.is_ObjectID(uid):
                raise Exception('Bad uid Format')
            user_data = yield self.db.users.find_one({'_id' : ObjectId(uid)})

            if not user_data:
                raise Exception('user not exist')

            # TODO : filter fields
            self.write_json({'result' : user_data})

        except Exception as e:
            self.set_status(500)
            self.finish({'error' : str(e)})

    


































