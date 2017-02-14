#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com


class Alarm(object):
    @classmethod
    def get_alarm_device(cls, db):
        sql = "SELECT * FROM alarm"
        return db.query(sql)

    @classmethod
    def update_alarm_device(cls, state, id, db):
        sql = "UPDATE alarm SET state = %s WHERE id = %s"
        return db.execute(sql, state, id)