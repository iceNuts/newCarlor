# encoding: utf-8
#
# User Model

from tornado import gen
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          SignatureExpired, BadSignature)
from mini import EnumField
from motorengine import (Document, StringField, DateTimeField,
                         BooleanField, EmailField)


class User(Document):
    first_name = StringField(max_length=20)
    last_name = StringField(max_length=20)
    birthday = DateTimeField()
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    phone = StringField(max_length=50)
    school = StringField(max_length=100)
    major = StringField(max_length=50)
    # F femail / M male
    gender = EnumField(options=['F', 'M', 'X'], default='X')
    signature = StringField()
    driver = BooleanField()
    email_active = BooleanField()
    phone_active = BooleanField()
    account_active = BooleanField()
    driver_license = StringField()
    # replace to reference field when those two Documents are changed
    car_id = StringField()   # has_a car => Car
    photo_id = StringField()   # has_a profilephoto => Photo

    INFO_FIELDS = [
        'email', 'first_name', 'last_name', 'phone',
        'school', 'major', 'gender', 'driver', 'driver_license',
        'car_id', 'photo_id',
    ]

    def create_token(self, secret, expiration=60000):
        s = Serializer(secret, expires_in=expiration)
        return s.dumps({'id': str(self._id)})

    def get_info(self):

        info = {k: getattr(self, k) for k in self.INFO_FIELDS}
        if self._id:
            info['id'] = str(self._id)

        return info

    @gen.coroutine
    def save_info(self, data):
        for k in self.INFO_FIELDS:
            if k in data:
                setattr(self, k, data[k])

        yield self.save()

    @staticmethod
    @gen.coroutine
    def get_user_by_email(email):
        users = yield User.objects.filter(email=email).find_all()
        if users and len(users):
            return users[0]

        return None

    @staticmethod
    @gen.coroutine
    def verify_token(token, secret):
        s = Serializer(secret)
        try:
            data = s.loads(token)
        except SignatureExpired:
            print('token expired')
            return None
        except BadSignature:
            print('bad token')
            return None
        user = yield User.objects.get(data['id'])

        return user
