#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_restful import Api
from apps.users.resources_admin import Stats
from apps.users.resources import SignUp
from apps.users.resources_admin import AdminUserPageList, AdminUserResource, UsersCadUrl


def configure_api(app):
    api = Api()
    api.add_resource(Stats, '/stats')
    api.add_resource(SignUp, '/users')
    api.add_resource(UsersCadUrl, '/users/<int:userid>/url')
    api.add_resource(AdminUserPageList, '/admin/users/<int:page_id>')
    api.add_resource(AdminUserResource, '/admin/users/<string:user_id>')
    api.init_app(app)
