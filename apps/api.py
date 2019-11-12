#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_restful import Api
from apps.users.resources import (
    Users,
    UsersDelete,
    UsersCadUrl,
    UrlsDelete,
    StatsID,
    Stats,
    UserStats
)


def configure_api(app):
    api = Api()
    api.add_resource(Users, '/users')
    api.add_resource(UsersDelete, '/users/<string:user_id>')
    api.add_resource(UsersCadUrl, '/users/<string:user_id>/url')
    api.add_resource(UrlsDelete, '/urls/<int:url_id>')
    api.add_resource(StatsID, '/stats/<int:url_id>')
    api.add_resource(Stats, '/stats')
    api.add_resource(UserStats, '/users/<string:user_id>/stats')

    api.init_app(app)
