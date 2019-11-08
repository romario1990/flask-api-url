#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_restful import Api
from apps.stats import stats

def configure_api(app):
    # Instânciando as API do FlaskRestful
    api = Api()
    # Adicionando rotas '/'
    api.add_resource(stats, '/stats')


    # Inicializamos a api
    api.init_app(app)