# encoding: utf-8
#
# User Model

from mini import Document
from datetime import datetime


class User(Document):
    first_name = str
    last_name = str
    birthday = datetime
    email = str
    password = str
    phone = str
    school = str
    major = str
    gender = str   # F femail / M male
    signature = str
    driver = bool
    email_active = bool
    phone_active = bool
    account_active = bool
    driver_license = str
    car_id = str   # has_a car => Car
    photo_id = str   # has_a profilephoto => Photo

    # OVERRIDE THIS TO PROTECT YOUR DATA
    # SET SOME DEFAULT VALUE
    def firewall(self, dirty_entries, options={}):

        return dirty_entries
