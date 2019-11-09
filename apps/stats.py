#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Third
from flask_restful import Resource


class stats(Resource):
    # Definição da operação get

    def get(self):
        return {'hello': 'statsGet'}
