#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: daichao@tigerbrokers.com

import time

import database


class History(object):
    """
    task_id
    process
    status
    path
    description
    user
    """
    def __init__(self):
        self.db = database.mongodb()

    @classmethod
    def new(cls, **kwargs):
        return database.mongodb().history.insert(kwargs)

    @classmethod
    def get_history_by_field(cls, **fields):
        return database.mongodb().history.find(fields, {'_id': 0})

    @classmethod
    def add_history(cls, **kwargs):
        kwargs['done_time'] = time.time()
        return database.mongodb().history.insert(kwargs)

    @classmethod
    def query_history(cls, query):
        return database.mongodb().history.find_one(query)
