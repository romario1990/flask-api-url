#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Python
from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())


class DevelopConfig(Config):
    FLASK_ENV = 'develop'
    DEBUG = True

class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True

config = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'default': DevelopConfig
}
