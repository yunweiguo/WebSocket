#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com


import json
import util
import router
from model import history


@router.Route("/ws/controller")
class ControllerHandler(util.BaseSocketHandler):
    def open(self):
        util.ProStatus().register(self)

    def on_message(self, message):
        msg = json.loads(message)
        device_id = msg.get("id")
        his = history.History.get_history_by_field({"id": device_id})
        data = {
            "msg_type": "history",
            "data": his
        }
        util.ProStatus().brocast(json.dumps(data, ensure_ascii=False))

    def on_close(self):
        util.ProStatus().unregister(self)
