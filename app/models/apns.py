# encoding: utf-8
#
# APNs Token Model
# A table for iOS device tokens

from motorengine import *

class APNs(Document):
    device_token        = StringField(required=True, unique=True)
    user_id             = StringField(required=True)
    aws_endpoint_arn    = StringField(required=True)

    # OVERRIDE THIS TO PROTECT YOUR DATA
    # SET SOME DEFAULT VALUE
    # CHECK KEY NAME
    # CONVERT TO PROPER TYPE
    @classmethod
    def firewall(self, dirty_entries, options={}):
        
        return dirty_entries

    # FILTER OUT SOME SENSITIVE FIELDS
    @classmethod
    def outputer(self, incoming, options={}):

        return incoming