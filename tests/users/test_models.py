#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mongoengine import (
    StringField,
    IntField)
from apps.users.models import User, Url, GeradorID


class TestUser:

    def setup_method(self):
        self.data = {
            'email': 'teste1@teste.com',
            'password': 'teste123',
            'name': 'Teste',
        }

        # Crio uma instancia do modelo User
        self.model = User(**self.data)

    def test_email_field_exists(self):
        # Verifico se o campo email existe
        assert 'email' in self.model._fields

    def test_email_field_is_required(self):
        # Verifico se o campo email é requirido
        assert self.model._fields['email'].required is True

    def test_email_field_is_str(self):
        # Verifico se o campo email é do tipo string
        assert isinstance(self.model._fields['email'], StringField)

    def test_name_field_exists(self):
        # Verifico se o campo name existe
        assert 'name' in self.model._fields

    def test_name_field_is_str(self):
        # Verifico se o campo name é do tipo string
        assert isinstance(self.model._fields['name'], StringField)

    def test_name_field_is_unique(self):
        # Verifico se o campo name é unico
        assert self.model._fields['name'].unique is True

    def test_all_fields_in_model(self):
        # Verifico se todos os campos estão de fato no meu modelo
        fields = [
            'email', 'name', 'id', 'password'
        ]

        model_keys = [i for i in self.model._fields.keys()]

        fields.sort()
        model_keys.sort()

        assert fields == model_keys


class TestUrl:

    def setup_method(self):
        self.data = {
            'idUrl': 1,
            'hits': 10,
            'url': "http://google.com",
            'short_url': "http://0.0.0.0:5000/gdsajh",
            'nameUser': "romario"
        }

        # Crio uma instancia do modelo Url
        self.model = Url(**self.data)

    def test_idUrl_field_exists(self):
        # Verifico se o campo
        assert 'idUrl' in self.model._fields

    def test_idUrl_field_is_required(self):
        # Verifico se o campo é requirido
        assert self.model._fields['idUrl'].required is True

    def test_idUrl_field_is_int(self):
        # Verifico se o campo é do tipo string
        assert isinstance(self.model._fields['idUrl'], IntField)

    def test_idUrl_field_is_unique(self):
        # Verifico se o campo é unico
        assert self.model._fields['idUrl'].unique is True

    def test_hits_field_exists(self):
        # Verifico se o campo existe
        assert 'hits' in self.model._fields

    def test_hits_field_is_required(self):
        # Verifico se o campo é requirido
        assert self.model._fields['hits'].required is True

    def test_hits_field_is_int(self):
        # Verifico se o campo é do tipo string
        assert isinstance(self.model._fields['hits'], IntField)

    def test_url_field_exists(self):
        # Verifico se o campo existe
        assert 'url' in self.model._fields

    def test_url_field_is_required(self):
        # Verifico se o campo é requirido
        assert self.model._fields['url'].required is True

    def test_url_field_is_str(self):
        # Verifico se o campo é do tipo string
        assert isinstance(self.model._fields['url'], StringField)

    def test_short_url_field_exists(self):
        # Verifico se o campo existe
        assert 'short_url' in self.model._fields

    def test_short_url_field_is_required(self):
        # Verifico se o campo é requirido
        assert self.model._fields['short_url'].required is True

    def test_short_url_field_is_str(self):
        # Verifico se o campo é do tipo string
        assert isinstance(self.model._fields['short_url'], StringField)

    def test_nameUser_field_exists(self):
        # Verifico se o campo existe
        assert 'nameUser' in self.model._fields

    def test_nameUser_field_is_required(self):
        # Verifico se o campo é requirido
        assert self.model._fields['nameUser'].required is True

    def test_nameUser_field_is_str(self):
        # Verifico se o campo é do tipo string
        assert isinstance(self.model._fields['nameUser'], StringField)


class TestGeradorID:

    def setup_method(self):
        self.data = {
            'id_tabela': 1,
            'name_tabela': "Url"
        }

        # Crio uma instancia do modelo Url
        self.model = GeradorID(**self.data)

    def test_id_tabela_field_exists(self):
        # Verifico se o campo
        assert 'id_tabela' in self.model._fields

    def test_id_tabela_field_is_required(self):
        # Verifico se o campo é requirido
        assert self.model._fields['id_tabela'].required is True

    def test_id_tabela_field_is_int(self):
        # Verifico se o campo é do tipo string
        assert isinstance(self.model._fields['id_tabela'], IntField)

    def test_name_tabela_field_exists(self):
        # Verifico se o campo
        assert 'name_tabela' in self.model._fields

    def test_name_tabela_field_is_required(self):
        # Verifico se o campo é requirido
        assert self.model._fields['name_tabela'].required is True

    def test_id_name_tabela_field_is_int(self):
        # Verifico se o campo é do tipo string
        assert isinstance(self.model._fields['name_tabela'], StringField)
