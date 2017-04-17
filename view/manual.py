#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

import json
import util
import datetime
from model import device, history
import router


@router.Route("/manual")
class ManualHandler(util.BaseHandler):
    def get(self):
        system = "manual"
        devices = device.Device.get_devices_by_system(system, self.db)
        result = dict(is_succ=True, data=devices)
        self.finish(json.dumps(result, ensure_ascii=False))

    def post(self, *args, **kwargs):
        system = "manual"
        device_type = self.get_argument("type")
        device_name = self.get_argument("device_name")
        state = self.get_argument("state")
        device_id = self.get_argument("id")
        device.Device.update_state(state, device_id, self.db)
        data = {
            "msg_type": "update",
            "data": {
                "id": device_id,
                "system": system,
                "type": device_type,
                "info": {
                    "state": state,
                }
            }
        }

        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        description = u"{}开始报警".format(device_name) if state == "on" else u"{}结束报警".format(device_name)
        new_history = {
            "id": device_id,
            "system": system,
            "type": device_type,
            "create_time": create_time,
            "description": description
        }
        history.History.add_history(**new_history)

        util.ProStatus().brocast(message=json.dumps(data, ensure_ascii=False))