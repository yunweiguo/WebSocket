#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

from pymongo import MongoClient
from torndb import Connection

MONGODB_URI = "mongodb://127.0.0.1:27017//websocket"
MONGODB_DB = "websocket"

MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_DB = "websocket"
MYSQL_PASSWORD = "yunweiguo"


def mysqldb(mysql_host=MYSQL_HOST, mysql_user=MYSQL_USER,
                   mysql_password=MYSQL_PASSWORD, mysql_db=MYSQL_DB):
    conn = Connection(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db
    )
    return conn


def mongodb(mongodb_uri=MONGODB_URI, mongodb_db=MONGODB_DB):
    conn = MongoClient(mongodb_uri)
    return conn[mongodb_db]
