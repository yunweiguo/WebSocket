#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

import json
import util
from model import equipment
import router


@router.Route("/manual")
class ManualHandler(util.BaseHandler):
    def get(self):
        equipments = equipment.Equipment.get_equipment(self.db)
        self.render("manual.html", data=equipments)

    def post(self, *args, **kwargs):
        equipment_id = self.get_argument("id")
        state = self.get_argument("state")
        equipment.Equipment.update_state(state, equipment_id, self.db)
        data = json.dumps({"id": equipment_id, "data": state, "type": "manual"}, ensure_ascii=False)
        util.ProStatus().brocast(message=data)

