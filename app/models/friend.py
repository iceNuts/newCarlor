# encoding: utf-8
#
# Friend Model

from motorengine import *

class Friend(Document):
    foo_uid     = StringField(required=True)
    bar_uid     = StringField(required=True)