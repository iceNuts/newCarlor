# encoding: utf-8
#
# Like Model

from mini import Document
from datetime import datetime
from bson import ObjectId

class Like(Document):
    liked_id        = str
    event_type      = str   # special or normal
    uid             = str   # who does it