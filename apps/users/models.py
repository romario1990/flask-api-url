#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mongoengine import (
    EmailField,
    StringField,
    IntField,
    ReferenceField,
)
from apps.db import db


class User(db.Document):
    meta = {'collection': 'users'}

    name = StringField(required=True, unique=True)
    email = EmailField(required=True)
    password = StringField(required=True)


class Url(db.Document):
    meta = {'collection': 'urls'}

    idUrl = IntField(required=True, unique=True)
    hits = IntField(required=True, fefault=1)
    url = StringField(required=True)
    short_url = StringField(required=True)
    nameUser = StringField(required=True)


class GeradorID(db.Document):
    meta = {'collection': 'GeradorID'}

    id_tabela = IntField(required=True)
    name_tabela = StringField(required=True)
