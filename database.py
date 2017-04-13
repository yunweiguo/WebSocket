#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

import pymongo
import torndb
import tornadoredis
import redis
import config


def connect():
    # connection_pool = tornadoredis.ConnectionPool(max_connections=config.MAX_CONNECTIONS,
    #                                               wait_for_available=True)
    return tornadoredis.Client(host=config.REDIS_HOST, port=config.REDIS_PORT,
                               selected_db=config.REDIS_DB, password=config.REDIS_PASSWORD)


def s_connect():
    connection_pool = redis.ConnectionPool(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB,
                                           password=config.REDIS_PASSWORD)
    return redis.Redis(connection_pool=connection_pool)


def mysqldb(mysql_host=config.MYSQL_HOST, mysql_user=config.MYSQL_USER,
                   mysql_password=config.MYSQL_PASSWORD, mysql_db=config.MYSQL_DB):
    conn = torndb.Connection(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db
    )
    return conn


def mongodb(mongodb_uri=config.MONGODB_URI, mongodb_db=config.MONGODB_DB):
    conn = pymongo.MongoClient(mongodb_uri)
    return conn[mongodb_db]


def single_connect():
    return tornadoredis.Client(host=config.REDIS_HOST, port=config.REDIS_PORT,
                               selected_db=config.REDIS_DB, password=config.REDIS_PASSWORD)