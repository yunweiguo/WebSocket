#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yunweiguo18789@gmail.com

import util
import router


@router.Route("/")
class MainHandler(util.BaseHandler):
    def get(self):
        self.render("index.html")


@router.Route("/index/parking")
class IndexParkingHandler(util.BaseHandler):
    def get(self):
        self.render("parking.html")


@router.Route("/index/dynamic")
class IndexDynamicHandler(util.BaseHandler):
    def get(self):
        self.render("dynamic.html")


@router.Route("/index/manual")
class IndexManualHandler(util.BaseHandler):
    def get(self):
        self.render("manual.html")


@router.Route("/index/controller")
class ControllerIndexHandler(util.BaseHandler):
    def get(self):
        self.render("controller.html")