#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

import logging
import tornado.web
import tornado.ioloop
import tornado.autoreload
import tornado.httpserver
import tornado.options
from tornado.ioloop import PeriodicCallback

import router
import config
import database
from view import *


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, router.Route.get_routes(), **config.settings)

        self.mysqldb = database.mysqldb()
        self.async_redis = database.connect()
        self.sync_redis = database.s_connect()


if __name__ == '__main__':
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(7000)

    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()

