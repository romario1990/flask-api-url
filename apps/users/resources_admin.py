#!/usr/bin/python3
# -*- coding: utf-8 -*-
import short_url
from flask import request
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist
from mongoengine.errors import NotUniqueError, ValidationError
from apps.responses import (
    resp_already_exists,
    resp_exception,
    resp_data_invalid,
    resp_ok
)
from apps.messages import (
    MSG_RESOURCE_FETCHED_PAGINATED,
    MSG_RESOURCE_FETCHED,
    MSG_INVALID_DATA,
    MSG_RESOURCE_DELETED,
    MSG_NO_DATA,
    MSG_RESOURCE_CREATED
)
from .models import User, Url
from .schemas import UserSchema, UserRegistrationUrlSchema, UserUpdateSchema
from .utils import get_user_by_id
import uuid


class AdminUserPageList(Resource):
    # Lembra-se do page_id criado na rota ele pode ser acessado como parâmetro
    # do metodo get
    def get(self, page_id=1):
        # inicializa o schema podendo conter varios objetos
        schema = UserSchema(many=True)
        # incializa o page_size sempre com 10
        page_size = 10

        # se enviarmos o page_size como parametro
        if 'page_size' in request.args:
            # verificamos se ele é menor que 1
            if int(request.args.get('page_size')) < 1:
                page_size = 10
            else:
                # fazemos um type cast convertendo para inteiro
                page_size = int(request.args.get('page_size'))

        try:
            # buscamos todos os usuarios da base utilizando o paginate
            # users = User.objects().paginate(page_id, page_size)
            users = User.objects().paginate(page_id, page_size)

        except FieldDoesNotExist as e:
            return resp_exception('Users', description=e.__str__())

        except StopIteration as e:
            return resp_exception('Users', description=e.__str__())

        except Exception as e:
            return resp_exception('Users', description=e.__str__())

        # criamos dados extras a serem respondidos
        extra = {
            'page': users.page, 'pages': users.pages, 'total': users.total,
            'params': {'page_size': page_size}
        }

        # fazemos um dump dos objetos pesquisados
        result = schema.dump(users.items)

        return resp_ok(
            'Users', MSG_RESOURCE_FETCHED_PAGINATED.format('usuários'), data=result.data,
            **extra
        )


class AdminUserResource(Resource):
    def get(self, user_id):
        schema = UserSchema()
        try:
            # Buscando usuário por id
            user = User.objects.get(id=user_id)
        except FieldDoesNotExist as e:
            return resp_exception('Users', description=e.__str__())
        except Exception as e:
            return resp_exception('Users', description=e.__str__())
        result = schema.dump(user)
        return resp_ok(
            'Users', MSG_RESOURCE_FETCHED.format('Usuários'), data=result.data
        )

    def delete(self, user_id):
        # Busco o usuário na coleção users pelo seu id
        user = get_user_by_id(user_id)

        # se não for uma instancia do modelo User retorno uma resposta
        # da requisição http do flask
        if not isinstance(user, User):
            return user

        try:
            user.active = False
            user.save()

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
        data, errors, result = None, None, None
        user_id = param_url['userid']
        schema = UserRegistrationUrlSchema()

        # Se meus dados postados forem Nulos retorno uma respota inválida
        if req_data is None:
            return resp_data_invalid('Users', [], msg=MSG_NO_DATA)

        # Desserialização os dados postados ou melhor meu payload
        data, errors = schema.load(req_data)

        # Se houver erros retorno uma resposta inválida
        if errors:
            return resp_data_invalid('Users', errors)

        try:
            model = Url(**data)
            model.id = uuid.uuid1()
            model.short_url = short_url.encode_url(data['url'])
            model.save()

        except NotUniqueError:
            return resp_already_exists('Users', 'url')

        except ValidationError as e:
            return resp_exception('Users', msg=MSG_INVALID_DATA, description=e)

        except Exception as e:
            return resp_exception('Users', description=e)

        schema = UserRegistrationUrlSchema()
        result = schema.dump(model)

        # Retorno 200 o meu endpoint
        return resp_ok(
            'Users', MSG_RESOURCE_CREATED.format('Url'), data=result.data,
        )



class Stats(Resource):
    def get(self):
        return {'hello': 'statsGet'}

