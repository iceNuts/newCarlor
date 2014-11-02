# encoding: utf-8
#
# web server main app

import tornado.ioloop
import tornado.web
import tornado.options

import logging
import motor
from motorengine import connect

import boto.sqs
import boto.sns

from tornado.httpserver import HTTPServer

""" Require API Controllers

    Serialize output data and handle incoming request
"""

from api import (UserHandler, AuthTokenHandler, ChatgroupHandler,
                 APNsHandler, MessageHandler)


""" Tornado App Configuration

"""


def aws_account():
    aws_access_id = 'AKIAIZURHIWICSIMGX7Q'
    aws_access_key = 'AvbGBYwVVsXsOoQUXhFKc6oRPdXF9cCbC0GBz7BC'

    return aws_access_id, aws_access_key


def get_url_list():

    return [
        # create a new user
        tornado.web.URLSpec(r'/api/v1/user/', UserHandler),
        # update a user info
        tornado.web.URLSpec(r'/api/v1/user/update', UserHandler),
        # get user info
        tornado.web.URLSpec(r'/api/v1/user/([a-zA-Z0-9]+)', UserHandler),
        tornado.web.URLSpec(r'/api/v1/token', AuthTokenHandler),

        # create a new user
        tornado.web.URLSpec(r'/api/v1/chatgroup/new', ChatgroupHandler),

        # create a new APNs
        tornado.web.URLSpec(r'/api/v1/apns/new', APNsHandler),

        # shoot a message to a chatgroup
        tornado.web.URLSpec(r'/api/v1/message/new', MessageHandler),
    ]


def get_settings():

    return {
        'secret': '_&xC#!~-2987UYWq|{RClubCIL}o><?[]axWERFC@',
        'expires': 360,
        'login_url': '/api/login',
        'debug': True
    }


def conn_db(io_loop):
    connect("carlor", io_loop=io_loop)


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
    sqs = get_sqs()
    sns = get_sns()

    application = tornado.web.Application(
        url_list,
        sqs=sqs,
        sns=sns,
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
    conn_db(ioloop)
    try:
        ioloop.start()
    except KeyboardInterrupt:
        stop_server(server)

    logging.info('--- club server stopped ---')


if __name__ == '__main__':
    main()
