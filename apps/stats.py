#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request

class stats(Resource):
    # Definição da operação get

    def get(self):
        return {'hello': 'statsGet'}

