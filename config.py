#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com


settings = {
    "debug": True,
    "template_path": "templates",
    "static_path": "static",
}

APP_PORT = 8000

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_PASSWORD = ""
MAX_CONNECTIONS = 1000

MONGODB_URI = "mongodb://127.0.0.1:27017//websocket"
MONGODB_DB = "websocket"

MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_DB = "websocket"
MYSQL_PASSWORD = "yunweiguo"