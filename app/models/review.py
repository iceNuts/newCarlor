# encoding: utf-8
#
# Review Model

from mini import Document
from datetime import datetime

class Review(Document):
    event_id    = str   # must be special event
    user_id     = str   # who wrote this
    time        = datetime
    detail      = str
    title       = str
    likes       = int