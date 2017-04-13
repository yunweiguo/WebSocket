#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com


class Device(object):
    """
    system        子系统名称
    type
    temperature   温度
    state         手动报警器状态 on, off
    """

    @classmethod
    def get_devices_by_system(cls, system, db):
        return db.query("SELECT * FROM device WHERE system = %s ORDER by type", system)

    @classmethod
    def update_parking_state(cls, state, device_id, db):
        return db.execute("UPDATE device SET state = %s WHERE id = %s", state, device_id)

    @classmethod
    def update_smoke(cls, smokescope, device_id, db):
        return db.execute("UPDATE device SET smokescope = %s WHERE id = %s ", smokescope, device_id)

    @classmethod
    def update_temperature(cls, temperature, device_id, db):
        return db.execute("UPDATE device SET temperature = %s WHERE id = %s",temperature, device_id)

    @classmethod
    def update_state(cls, state, device_id, db):
        return db.execute("UPDATE device SET state = %s WHERE id = %s", state, device_id)

