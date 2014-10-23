# encoding: utf-8
#
# APNs Token Model
# A table for iOS device tokens

from mini import Document


class APNs(Document):
    device_token = str
    user_id = str
    aws_endpoint_arn = str
