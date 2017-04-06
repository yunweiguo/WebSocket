#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

import json
import util
from model import device, equipment


class SmokeHandler(util.BaseHandler):
    def get(self):
        equipments = equipment.Equipment.get_equipment(self.db)
        self.render("smoke.html", data=equipments)

    def post(self, *args, **kwargs):
        equipment_id = self.get_argument("id")
        smokescope = self.get_argument("smokescope")
        equipment.Equipment.update_smoke(smokescope, equipment_id, self.db)
        data = json.dumps({"id": equipment_id, "data": smokescope, "type": "smoke"}, ensure_ascii=False)
        util.ProStatus().brocast(message=data)

