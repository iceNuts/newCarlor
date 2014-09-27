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

from tornado.httpserver import HTTPServer

from controllers import IndexHandler
from controllers import UsersHandler
from controllers import CommentsHandler
from controllers import CommentedHandler
from controllers import ChatgroupsHandler
from controllers import MessagesHandler

def get_url_list():

    url_list = [
        # Debug Request
        tornado.web.URLSpec(r'/', IndexHandler, name='index'),

        # Dev Request

        # Create User
        tornado.web.URLSpec(r'/api/v1/user/new', UsersHandler, name='users'),
        
        # Create event Comment
        tornado.web.URLSpec(r'/api/v1/event/([a-zA-Z0-9]+)/comment/new', CommentsHandler, name='comments'),

        # Put/Delete event Comment
        tornado.web.URLSpec(r'/api/v1/event/([a-zA-Z0-9]+)/comment/([a-zA-Z0-9]+)', CommentsHandler, name='comments'),

        # Get event Comments
        tornado.web.URLSpec(r'/api/v1/event/([a-zA-Z0-9]+)/comments/([0-9]+)', CommentsHandler, name='comments'),

        # Get event Commented
        tornado.web.URLSpec(r'/api/v1/event/([a-zA-Z0-9]+)/commented/([0-9]+)', CommentedHandler, name='commented'),

        # Put/Get User
        tornado.web.URLSpec(r'/api/v1/user/([a-zA-Z0-9]+)', UsersHandler, name='users'),

        # Create a chat group
        tornado.web.URLSpec(r'/api/v1/chatgroup', ChatgroupsHandler, name='chatgroups'),

        # Update / Get / Delete a chat group
        tornado.web.URLSpec(r'/api/v1/chatgroup/([a-zA-Z0-9]+)', ChatgroupsHandler, name='chatgroups'),

        # Create a message
        tornado.web.URLSpec(r'/api/v1/chatgroup/([a-zA-Z0-9]+)/message', MessagesHandler, name='messages'),

    ]

    return url_list

def get_settings():

    settings = {
        'cookie_secret': '_&xC#!~-2987UYWq|{RClubCIL}o><?[]axWERFC@',
        'login_url': '/api/login',
        'debug': True
    }

    return settings

def get_db():

    db = motor.MotorClient().carlor
    return db

def get_app():

    url_list = get_url_list()
    settings = get_settings()
    db = get_db()

    application = tornado.web.Application(
        url_list,
        db=db,
        **settings
        )
    
    return application


def get_ioloop():

    ioloop = tornado.ioloop.IOLoop.instance()
    return ioloop


def stop_server(server):

    logging.info('--- stopping club server ---')
    server.stop()


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
