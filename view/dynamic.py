#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

import json
import util
from model import device
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
        state = self.get_argument("state")
        device_id = self.get_argument("id")
        temperature = self.get_argument("temperature", "")
        smokescope = self.get_argument("smokescope", "")
        device.Device.update_parking_state(device_type, state, self.db)
        data = {
            "id": device_id,
            "system": system,
            "type": device_type,
            "info": {
                "temperature": temperature,
                "smokescope": smokescope
            }
        }
        util.ProStatus().brocast(message=json.dumps(data, ensure_ascii=False))


