#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com


class Equipment(object):
    """
    location      地点
    smokescope    烟雾浓度
    temperature   温度
    state         手动报警器状态 on, off
    """

    @classmethod
    def get_equipment(cls, db):
        return db.query("SELECT * FROM equipment")

    @classmethod
    def update_smoke(cls, smokescope, equipment_id, db):
        return db.execute("UPDATE equipment SET smokescope = %s WHERE id = %s ", smokescope, equipment_id)

    @classmethod
    def update_temperature(cls, temperature, equipment_id, db):
        return db.execute("UPDATE equipment SET temperature = %s WHERE id = %s",temperature, equipment_id)

    @classmethod
    def update_state(cls, state, equipment_id, db):
        return db.execute("UPDATE equipment SET state = %s WHERE id = %s", state, equipment_id)

