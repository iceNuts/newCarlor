# encoding: utf-8
#   
# web server main app

import tornado.ioloop
import tornado.web
import tornado.options

import functools
import logging
import signal
import time
import motor
import boto.sqs
import boto.sns

from tornado.httpserver import HTTPServer

""" Require API Controllers
    
    Serialize output data and handle incoming request
"""

from api import UserHandler
from api import ChatgroupHandler
from api import APNsHandler


""" Tornado App Configuration

"""

def aws_account():
    aws_access_id = 'AKIAIZURHIWICSIMGX7Q'
    aws_access_key = 'AvbGBYwVVsXsOoQUXhFKc6oRPdXF9cCbC0GBz7BC'

    return aws_access_id, aws_access_key


def get_url_list():

    return [
        #create a new user
        tornado.web.URLSpec(r'/api/v1/user/new', UserHandler),
        # update a user info
        tornado.web.URLSpec(r'/api/v1/user/update', UserHandler),
        # get user info
        tornado.web.URLSpec(r'/api/v1/user/([a-zA-Z0-9]+)', UserHandler),

        #create a new user
        tornado.web.URLSpec(r'/api/v1/chatgroup/new', ChatgroupHandler),
    
        #create a new APNs
        tornado.web.URLSpec(r'/api/v1/apns/new', APNsHandler),
    ]


def get_settings():

    return {
        'cookie_secret': '_&xC#!~-2987UYWq|{RClubCIL}o><?[]axWERFC@',
        'login_url': '/api/login',
        'debug': True
    }


def get_db():

    return motor.MotorClient().carlor 

def get_sqs():
    
    aws_access_id, aws_access_key = aws_account()

    conn = boto.sqs.connect_to_region(
        'us-west-2',
        aws_access_key_id=aws_access_id,
        aws_secret_access_key=aws_access_key)
    return conn

def get_sns():

    aws_access_id, aws_access_key = aws_account()

    conn = boto.sns.connect_to_region(
        'us-west-2',
        aws_access_key_id=aws_access_id,
        aws_secret_access_key=aws_access_key)
    return conn

def get_app():

    url_list = get_url_list()
    settings = get_settings()
    db = get_db()
    sqs = get_sqs()
    sns = get_sns()

    application = tornado.web.Application (
        url_list,
        db = db,
        sqs = sqs,
        sns = sns,
        **settings
    )
    
    return application

def get_ioloop():

    ioloop = tornado.ioloop.IOLoop.instance()
    return ioloop


def stop_server(server):

    logging.info('--- stopping club server ---')
    server.stop()



""" Tornado server run loop
    
"""

def main():

    application = get_app()
    tornado.options.parse_command_line()
    server = HTTPServer(application)
    server.listen(80)
    ioloop = get_ioloop()
    try:
        ioloop.start()
    except KeyboardInterrupt:
        stop_server(server)

    logging.info('--- club server stopped ---')


if __name__=='__main__':
    main()


