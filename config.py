#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Python
from os import getenv

class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())


class DevelopmentConfig(Config):
    FLASK_ENV = 'develop'
    DEBUG = True


config = {
    'develop': DevelopmentConfig,
    'default': DevelopmentConfig
}