#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from config import config
from .api import configure_api


def create_app(config_name):
    app = Flask('api-url')
    app.config.from_object(config[config_name])
    configure_api(app)
    return app