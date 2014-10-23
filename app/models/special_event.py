# encoding: utf-8
#
# SpecialEvent Model

from mini import Document
from datetime import datetime


class SpecialEvent(Document):
    name = str
    detail = str
    location = dict
    start_time = datetime
    end_time = datetime
    photo_id = str
    capacity = int
    likes = int
    additionals = dict  # like discount
    members = list  # user ids
