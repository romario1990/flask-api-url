#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Python
from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    HOST = getenv('HOST')
    PORT = int(getenv('PORT'))
    DEBUG = eval(getenv('DEBUG').title())
    MONGODB_HOST = getenv('MONGODB_URI_TEST')


class DevelopConfig(Config):
    FLASK_ENV = 'develop'
    DEBUG = True


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    MONGODB_HOST = getenv('MONGODB_URI_TEST')

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    TESTING = False
    DEBUG = False

config = {
    'production': ProductionConfig,
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'default': DevelopConfig
}
