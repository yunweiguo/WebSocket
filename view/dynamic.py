#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

import json
import util
import datetime
from model import device, history
import router


@router.Route("/dynamic")
class ParkingHandler(util.BaseHandler):
    def get(self):
        system = "dynamic"
        devices = device.Device.get_devices_by_system(system, self.db)
        result = dict(is_succ=True, data=devices)
        self.finish(json.dumps(result, ensure_ascii=False))

    def post(self):
        system = "dynamic"
        device_type = self.get_argument("type")
        device_name = self.get_argument("device_name")
        device_id = self.get_argument("id")
        if device_type == 'temperature':
            temperature = self.get_argument("temperature")
            info = {"temperature": temperature}
            device.Device.update_temperature(temperature, device_id, self.db)
            description = u"{}检测到温度浓度为{}".format(device_name, temperature)
        elif device_type == 'smoke':
            smokescope = self.get_argument("smokescope")
            info = {"smokescope": smokescope}
            device.Device.update_smoke(smokescope, device_id, self.db)
            description = u"{}监测到烟雾浓度为{}".format(device_name, smokescope)
        data = {
            "msg_type": "update",
            "data": {
                "id": device_id,
                "system": system,
                "type": device_type,
                "info": info
            }
        }

        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_history = {
            "id": device_id,
            "system": system,
            "type": device_type,
            "create_time": create_time,
            "description": description
        }
        history.History.add_history(**new_history)

        util.ProStatus().brocast(message=json.dumps(data, ensure_ascii=False))
