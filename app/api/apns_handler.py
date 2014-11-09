# encoding: utf-8

""" COMMON DEPENDENCIES """

import tornado
from tornado import gen
from mini import BaseHandler
from bson import ObjectId

""" COMMON DEPENDENCIES """

from models import APNs
from mini import aws

class APNsHandler(BaseHandler):

    # create a new APNs and subscribe to AWS App
    @gen.coroutine
    def post(self):
        clean_data = APNs.firewall(self.data)
        arn = yield aws.app_add_endpoint(self, clean_data['device_token'])
        clean_data['aws_endpoint_arn'] = arn
        new_apns = APNs.from_son(clean_data)
        new_apns.validate()
        yield new_apns.save()
        self.write_json({'result' : 'OK'})

    # delete APNs and unsubscribe to AWS App
    @gen.coroutine
    def delete(self, device_token=''):
        entry = {'device_token' : device_token}
        clean_data = APNs.firewall(entry)
        query = Q(device_token=clean_data['device_token'])
        apns = yield APNs.objects.filter(query).find_all()
        right_apns = apns[0]
        yield aws.app_delete_endpoint(self, right_apns.aws_endpoint_arn)
        yield right_apns.delete()
        self.write_json({'result' : 'OK'})
        
    # Whenever user login  
    # We need register user's device to app list
    # Add the arn to all associated topics