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
from model.alarm import Alarm
from model.parking import Parking
from view.parking import ParkingHandler
from view.alarm import AlarmHandler


class Application(tornado.web.Application):
    def __init__(self, route, **kwargs):
        tornado.web.Application.__init__(self, route, **kwargs)
        self.mysqldb = database.mysqldb()


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.mysqldb


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class ParkingIndexHandler(BaseHandler):
    def get(self):
        parking_spaces = Parking.get_all_parking_space(self.db)
        self.render("parking.html", data=parking_spaces)


class AlarmIndexHandler(BaseHandler):
    def get(self):
        alarm_devices = Alarm.get_alarm_device(self.db)
        print alarm_devices
        self.render("alarm.html", data=alarm_devices)


if __name__ == '__main__':
    tornado.options.define("port", default=config.APP_PORT, type=int)
    tornado.options.parse_command_line()

    application = Application([
        (r'/', MainHandler),
        (r'/index/parking', ParkingIndexHandler),
        (r'/index/alarm', AlarmIndexHandler),
        (r'/parking', ParkingHandler),
        (r'/alarm', AlarmHandler)
    ], **config.settings)

    application.listen(7000)
    tornado.ioloop.IOLoop.instance().start()
