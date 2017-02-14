#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

from tornado import websocket
import json
import datetime
import router
from model import parking, database

CONNECTED_CLIENTS = []
mysqldb = database.mysqldb()


@router.Route("/parking")
class ParkingHandler(websocket.WebSocketHandler):
    def open(self):
        CONNECTED_CLIENTS.append(self)

    def on_message(self, message):
        data = json.loads(message)
        parking_id = data.get('id')
        state = data.get('state')
        if state == "busy":
            start_time = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
        else:
            start_time = "/"
        parking.Parking.update_state(parking_id, state, start_time, mysqldb)
        self.broadcast(json.dumps({'id': parking_id, 'state': state, "start_time": start_time}))

    def on_close(self):
        CONNECTED_CLIENTS.remove(self)

    @staticmethod
    def broadcast(message):
        for c in CONNECTED_CLIENTS:
            c.write_message(message)

