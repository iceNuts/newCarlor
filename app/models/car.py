# encoding: utf-8
#
# Car Model

from mini import Document


class Car(Document):
    user_id = str  # user id
    brand = str
    color = str
    plate = str
    capacity = int
