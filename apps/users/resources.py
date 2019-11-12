# -*- coding:utf-8 -*-

from flask import request
from flask_restful import Resource
from mongoengine.errors import NotUniqueError, ValidationError
from apps.responses import (
    resp_already_exists,
    resp_exception,
    resp_data_invalid,
    resp_ok,
    resp_ok_created, resp_does_not_exist, resp_ok_created_url)
from apps.messages import MSG_NO_DATA, MSG_INVALID_DATA, MSG_RESOURCE_DELETED
from apps.messages import MSG_RESOURCE_CREATED
from apps.users.utils import incrementId, get_url_by_idUrl, getTotalHits, getTotalHitsUser
from .models import User, Url, GeradorID
from .schemas import UserRegistrationSchema, UserSchema, UserRegistrationUrlSchema, UrlSchema
from .utils import get_user_by_id, get_url_by
import short_url


class Users(Resource):
    def post(self, *args, **kwargs):
        req_data = request.get_json() or None
        data, errors, result = None, None, None
        schema = UserRegistrationSchema()

        if req_data is None:
            return resp_data_invalid('Users', [], msg=MSG_NO_DATA)
        data, errors = schema.load(req_data)
        if errors:
            return resp_data_invalid('Users', errors)
        try:
            data['email'] = data['email'].lower()
            model = User(**data)
            model.save()
        except NotUniqueError:
            # Retorno 409 conflito
            return resp_already_exists('Users', 'usuário')
        except ValidationError as e:
            return resp_exception('Users', msg=MSG_INVALID_DATA, description=e.__str__())
        except Exception as e:
            return resp_exception('Users', description=e.__str__())
        schema = UserSchema()
        result = schema.dump(model)
        # Retorno 201 created
        return resp_ok_created(
            'Users', MSG_RESOURCE_CREATED.format('Usuário'), data=result.data
        )


class UsersDelete(Resource):
    def delete(self, user_id):
        user = get_user_by_id(user_id)
        if not isinstance(user, User):
            return user
        try:
            user.delete()
        except NotUniqueError:
            return resp_already_exists('Users', 'usuário')
        except ValidationError as e:
            return resp_exception('Users', msg=MSG_INVALID_DATA, description=e.__str__())
        except Exception as e:
            return resp_exception('Users', description=e.__str__())
        return resp_ok('Users', MSG_RESOURCE_DELETED.format('Usuário'))


class UsersCadUrl(Resource):
    def post(self, *args, **kwargs):
        param_url = kwargs
        req_data = request.get_json() or None
        data, errors, result, model = None, None, None, None
        schema = UserRegistrationUrlSchema()
        user = get_user_by_id(param_url["user_id"])
        if not isinstance(user, User):
            # Usuário enexistente
            return resp_does_not_exist('Users', 'Usuário')
        # Se meus dados postados forem Nulos retorno uma respota inválida
        if req_data is None:
            return resp_data_invalid('Users', [], msg=MSG_NO_DATA)
        # Desserialização os dados postados ou melhor meu payload
        data, errors = schema.load(req_data)
        # Se houver erros retorno uma resposta inválida
        if errors:
            return resp_data_invalid('Users', errors)
        try:
            dataLocal = get_url_by(data["url"])
            if not isinstance(dataLocal, Url):
                dataLocal = {"idUrl": 0, "hits": 0, "short_url": "", "nameUser": ""}
                dataLocal["idUrl"] = GeradorID.objects.count() + 1
                dataLocal["hits"] = 1
                dataLocal["short_url"] = "http://0.0.0.0:5000/" + short_url.encode_url(Url.objects.count() + 1)
                dataLocal["nameUser"] = param_url["user_id"]
                # TO_DO implementar controle de transação. Para executar o programa em mais de uma instância
                data.update(dataLocal)
                model = Url(**data)
                model.save()
            else:
                dataLocal.hits = dataLocal["hits"] + 1
                dataLocal.save()
        except NotUniqueError:
            return resp_already_exists('Urls', 'url')
        except ValidationError as e:
            return resp_exception('Urls', msg=MSG_INVALID_DATA, description=e)
        except Exception as e:
            return resp_exception('Urls', description=e)
        schema = UrlSchema()
        if model == None:
            result = schema.dump(dataLocal)
            # Retorno 200
            return resp_ok(
                'Users', MSG_RESOURCE_CREATED.format('Url'), data=result.data,
            )
        else:
            incrementId("url")
            result = schema.dump(model)
            # Retorno 201
            return resp_ok_created_url(
                'Users', MSG_RESOURCE_CREATED.format('Url'), data=result.data,
            )


class UrlsDelete(Resource):
    def delete(self, url_id):
        url = get_url_by_idUrl(url_id)
        if not isinstance(url, Url):
            return url
        try:
            url.delete()
        except NotUniqueError:
            return resp_already_exists('Urls', 'Url')
        except ValidationError as e:
            return resp_exception('Urls', msg=MSG_INVALID_DATA, description=e.__str__())
        except Exception as e:
            return resp_exception('Urls', description=e.__str__())


class StatsID(Resource):
    def get(self, url_id):
        dataLocal = get_url_by_idUrl(url_id)
        if not isinstance(dataLocal, Url):
            return resp_does_not_exist('Urls', 'url')
        schema = UrlSchema()
        result = schema.dump(dataLocal)
        # Retorno 200
        return resp_ok(
            'Urls', MSG_RESOURCE_CREATED.format('Url'), data=result.data,
        )


class Stats(Resource):
    def get(self):
        dataLocal = Url.objects.order_by('-hits')
        schema = UrlSchema()
        urls = []
        urlsSchema = {"hits": 0, "urlCount": 0, "topUrls": []}
        urlsSchema["hits"] = getTotalHits()
        urlsSchema["urlCount"] = Url.objects.count()
        for i in range(10):
            if i < Url.objects.count():
                if not isinstance(dataLocal[i], Url):
                    return resp_does_not_exist('Urls', 'url')
                url, erros = schema.dump(dataLocal[i])
                urls.append(url)
        urlsSchema["topUrls"] = urls
        # Retorno 200
        return resp_ok(
            'Urls', MSG_RESOURCE_CREATED.format('Url'), data=urlsSchema,
        )


class UserStats(Resource):
    def get(self, user_id):
        user = get_user_by_id(user_id)
        if not isinstance(user, User):
            return resp_does_not_exist('Users', 'Usuário')

        dataLocal = Url.objects.filter(nameUser=user_id).order_by('-hits')

        schema = UrlSchema()
        urls = []
        urlsSchema = {"hits": 0, "urlCount": 0, "topUrls": []}
        urlsSchema["hits"] = getTotalHitsUser(user_id)
        urlsSchema["urlCount"] = Url.objects.filter(nameUser=user_id).count()
        for i in range(10):
            if i < Url.objects.filter(nameUser=user_id).count():
                if not isinstance(dataLocal[i], Url):
                    return resp_does_not_exist('Urls', 'url')
                url, erros = schema.dump(dataLocal[i])
                urls.append(url)
        urlsSchema["topUrls"] = urls
        # Retorno 200
        return resp_ok(
            'Urls', MSG_RESOURCE_CREATED.format('Url'), data=urlsSchema,
        )

