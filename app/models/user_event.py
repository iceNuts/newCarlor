# encoding: utf-8
#
# UserEvent Model

from mini import Document
from datetime import datetime

class UserEvent(Document):
    name            = str
    host_user_id    = str   #  user id
    detail          = str
    location        = dict  #  2dsphere
    start_time      = datetime
    end_time        = datetime
    photo_id        = str
    capacity        = int
    likes           = int


