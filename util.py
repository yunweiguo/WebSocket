#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

import tornado.web
import tornado.websocket


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.mysqldb


class BaseSocketHandler(tornado.websocket.WebSocketHandler):
    @property
    def connect(self):
        return self.application.async_redis

    @property
    def s_connect(self):
        return self.application.sync_redis

    @property
    def db(self):
        return self.application.mysqldb


class ProStatus(object):
    w_client = []

    def register(self, callbacker):
        self.w_client.append(callbacker)

    def unregister(self, callbacker):
        self.w_client.remove(callbacker)

    def brocast(self, message):
        for client in self.w_client:
            client.write_message(message)