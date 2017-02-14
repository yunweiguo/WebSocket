#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com


class Parking(object):
    @classmethod
    def get_all_parking_space(cls, db):
        sql = "SELECT * from parking"
        return db.query(sql)

    @classmethod
    def update_state(cls, id, state, start_time, db):
        sql = "UPDATE parking set state = %s , start_time = %s WHERE id=%s"
        return db.execute(sql, state, start_time, id)
