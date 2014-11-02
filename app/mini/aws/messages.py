# encoding: utf-8

import tornado
from tornado import gen
import calendar
import hashlib
from datetime import datetime
from bson import ObjectId

# shoot a message to chatgroup


@gen.coroutine
def shoot_message(self):
    chatgroup_id = self.data['chatgroup_id']
    chatgroup = yield self.db.ChatGroup.find_one({'_id': ObjectId(chatgroup_id)})
    topic_arn = chatgroup['topic_arn']
    message = self.data['message']
    message_attributes = self.data['message_attributes']
    self.sns.publish(
        topic_arn,
        message,
        message_attributes
    )

# add an endpoint to application


@gen.coroutine
def app_add_endpoint(self, apns):
    aws_ios_app_arn = 'arn:aws:sns:us-west-2:878165105740:app/APNS_SANDBOX/CarlorDev'
    response = self.sns.create_platform_endpoint(
        aws_ios_app_arn,
        self.data['device_token']
    )
    aws_endpoint_arn = response['CreatePlatformEndpointResponse'][
        'CreatePlatformEndpointResult']['EndpointArn']
    data = {
        'aws_endpoint_arn': aws_endpoint_arn
    }
    apns.update(data)


@gen.coroutine
def app_delete_endpoint(self):
    # delete_endpoint
    pass

# create a topic and direct it to an app


@gen.coroutine
def create_topic(self, chatgroup):
    current_timestamp = calendar.timegm(datetime.utcnow().utctimetuple())
    topic_var = self.data['name'].encode(
        'utf-8') + str(current_timestamp).encode('utf-8')
    stored_topic_name = hashlib.md5(topic_var).hexdigest()
    response = self.sns.create_topic(stored_topic_name)
    topic_arn = response['CreateTopicResponse'][
        'CreateTopicResult']['TopicArn']
    data = {
        'topic_arn': topic_arn,
        'stored_topic_name': stored_topic_name
    }
    chatgroup.update(data)


@gen.coroutine
def subscribe_topic(self, topic_arn, subscribers):
    for subscriber in subscribers:
        self.sns.subscribe(
            topic_arn,
            subscriber['protocol'],
            subscriber['endpoint'])
