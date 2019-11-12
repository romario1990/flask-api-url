#!/usr/bin/python3
# -*- coding: utf-8
from mongoengine.errors import FieldDoesNotExist, DoesNotExist, MultipleObjectsReturned
from apps.responses import resp_exception, resp_does_not_exist, resp_data_invalid
from apps.users.models import GeradorID
from apps.users.schemas import GeradorIDSchema, UrlSchema
from .models import User, Url


def get_user_by_id(user_id: str):
    try:
        # buscamos todos os usuários da base utilizando o paginate
        return User.objects.get(name=user_id)

    except DoesNotExist:
        return resp_does_not_exist('Users', 'Usuário')

    except FieldDoesNotExist as e:
        return resp_exception('Users', description=e.__str__())

    except Exception as e:
        return resp_exception('Users', description=e.__str__())


def get_url_by(url_id: str):
    try:
        # buscamos todos os usuários da base utilizando o paginate
        return Url.objects.get(url=url_id)

    except DoesNotExist:
        return resp_does_not_exist('Urls', 'Url')

    except FieldDoesNotExist as e:
        return resp_exception('Urls', description=e.__str__())

    except Exception as e:
        return resp_exception('Urls', description=e.__str__())


def get_url_by_idUrl(url_id: str):
    try:
        # buscamos todos os usuários da base utilizando o paginate
        return Url.objects.get(idUrl=url_id)

    except DoesNotExist:
        return resp_does_not_exist('Urls', 'Url')

    except FieldDoesNotExist as e:
        return resp_exception('Urls', description=e.__str__())

    except Exception as e:
        return resp_exception('Urls', description=e.__str__())


def incrementId(tabela):
    schema = GeradorIDSchema()
    dataGerador = {"id_tabela": 0, "name_tabela": tabela}
    dataGerador, errors = schema.load(dataGerador)
    # Se houver erros retorno uma resposta inválida
    if errors:
        return resp_data_invalid('Urls', errors)
    # TO_DO implemetar getMax do document DeradorID para distribuir id entre as tabelas
    dataGerador["id_tabela"] = GeradorID.objects.count() + 1
    modelGerador = GeradorID(**dataGerador)
    modelGerador.save()


def getTotalHits():
    dataLocal = Url.objects.order_by('-hits')
    schema = UrlSchema()
    totalHists = 0
    for i in range(len(dataLocal)):
        url, erros = schema.dump(dataLocal[i])
        totalHists = url["hits"] + totalHists

    return totalHists


def getTotalHitsUser(user_id):
    dataLocal = Url.objects.filter(nameUser=user_id).order_by('-hits')
    schema = UrlSchema()
    totalHists = 0
    for i in range(len(dataLocal)):
        url, erros = schema.dump(dataLocal[i])
        totalHists = url["hits"] + totalHists

    return totalHists
