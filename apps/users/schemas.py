#!/usr/bin/python3
# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Email, Str, Int
from apps.messages import MSG_FIELD_REQUIRED


class UserRegistrationUrlSchema(Schema):
    url = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )


class UserRegistrationSchema(Schema):
    name = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    email = Email(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    password = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )


class UserSchema(Schema):
    id = Str()
    name = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    email = Email(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )


class UrlSchema(Schema):
    idUrl = Int(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    hits = Int(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    url = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    short_url = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )


class GeradorIDSchema(Schema):
    id_tabela = Int(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    name_tabela = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
