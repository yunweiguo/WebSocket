#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

from tornado import websocket
import json
import router
from model import alarm
from model import database

CONNECTED_CLIENTS = []
mysqldb = database.mysqldb()


@router.Route("/alarm")
class AlarmHandler(websocket.WebSocketHandler):
    def open(self):
        CONNECTED_CLIENTS.append(self)

    def on_message(self, message):
        data = json.loads(message)
        alarm_id = data.get('id')
        state = data.get('state')
        alarm.Alarm.update_alarm_device(state, alarm_id, mysqldb)
        self.broadcast(json.dumps({"id": alarm_id, "state": state}))

    def on_close(self):
        CONNECTED_CLIENTS.remove(self)

    @staticmethod
    def broadcast(message):
        for c in CONNECTED_CLIENTS:
            c.write_message(message)
