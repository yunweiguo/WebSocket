#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

import tornado.web
import tornado.options
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.autoreload
import config
from model import database
from view.controller import ControllerHandler
from view.manual import ManualHandler
from view.smoke import SmokeHandler
from view.temperature import TemperatureHandler
import util
from model import equipment


class Application(tornado.web.Application):
    def __init__(self, route, **kwargs):
        tornado.web.Application.__init__(self, route, **kwargs)
        self.mysqldb = database.mysqldb()
        self.async_redis = database.connect()
        self.sync_redis = database.s_connect()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class ControllerIndexHandler(util.BaseHandler):
    def get(self):
        equipments = equipment.Equipment.get_equipment(self.db)
        self.render("controller.html", data=equipments)


if __name__ == '__main__':
    tornado.options.define("port", default=config.APP_PORT, type=int)
    tornado.options.parse_command_line()

    application = Application([
        (r'/', MainHandler),
        (r'/controller', ControllerIndexHandler),
        (r'/manual',  ManualHandler),
        (r'/smoke', SmokeHandler),
        (r'/temperature', TemperatureHandler),
        (r'/ws/controller', ControllerHandler)
    ], **config.settings)

    application.listen(7000)
    tornado.ioloop.IOLoop.instance().start()
