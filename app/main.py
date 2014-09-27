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

""" Require API Controllers
    
    Serialize output data and handle incoming request
"""




""" Tornado App Configuration

"""


def get_url_list():

    return [

    ]


def get_settings():

    return {
        'cookie_secret': '_&xC#!~-2987UYWq|{RClubCIL}o><?[]axWERFC@',
        'login_url': '/api/login',
        'debug': True
    }


def get_db():

    return motor.MotorClient().carlor 


def get_app():

    url_list = get_url_list()
    settings = get_settings()
    db = get_db()

    application = tornado.web.Application (
        url_list,
        db = db,
        **settings
    )
    
    return application


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


