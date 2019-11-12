#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json


def test_stats_content_get_response(client):
    """
    **Given** Luiz está acessando a API,
    **When** informa a rota/endpoint `/stats`,
    **Then** a api deve retorna estatísticas globais do sistema.
    **And** seu conteúdo deve ser
        {
            "hits": 193841,
            "urlCount": 2512,
            "topUrls": [
                {
                    "id": "23094",
                    "hits": 153,
                    "url": "http://www.chaordic.com.br/folks",
                    "shortUrl": "http://<host>[:<port>]/asdfeiba"
                },
                {
                    "id": "23090",
                    "hits": 89,
                    "url": "http://www.chaordic.com.br/chaordic",
                    "shortUrl": "http://<host>[:<port>]/asdfeiba"
                },
            ]
        }
    """
    # Realiza uma requisição HTTP do tipo get para o endpoint /
    response = client.get('/stats')

    data = json.loads(response.data.decode('utf-8'))

    # Fazemos o teste de asserção
    assert data['hits'] >= 0
    assert data['urlCount'] >= 0


def test_users_cadastro(client):
    """
    **Given** Luiz está acessando a API,
    **When** informa a rota/endpoint `/users`,
    **Then** a api deve cadastra um novo usuário.
    **And** seu conteúdo de envio deve ser
        {
            "name": "romario",
            "email": "romario@teste.com",
            "password": "123456"
        }
    **And** resposta deve ser
        {
          "id": "romario"
        }
    """
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    # Realiza uma requisição HTTP do tipo delete antes de cadastrar um novo para o endpoint /
    client.delete('/users/romario')

    # Realiza uma requisição HTTP do tipo post para o endpoint /
    data = """{
                    "name": "romario",
                    "email": "romario@teste.com",
                    "password": "123456"
                }
            """
    response = client.post('/users', data=data, headers=headers)

    data = json.loads(response.data.decode('utf-8'))

    # Fazemos o teste de asserção
    assert response.content_type == mimetype
    assert 'id' in data
    assert data['id'] == "romario"


def test_users_cadastrar_user_existente(client):
    """
    **Given** Luiz está acessando a API,
    **When** informa a rota/endpoint `/users`, onde o usuário já esta cadastrado
    **Then** a api deve retornar uma mensagem.
    **And** seu conteúdo de envio deve ser
        {
            "name": "romario",
            "email": "romario@teste.com",
            "password": "123456"
        }
    **And** resposta deve ser
        {
          "message": "Já existe um(a) usuário com estes dados.",
          "resource": "Users"
        }
    """
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    # Realiza uma requisição HTTP do tipo post para o endpoint /
    data = """{
                    "name": "romario",
                    "email": "romario@teste.com",
                    "password": "123456"
                }
            """

    # Realiza uma requisição HTTP do tipo delete para o endpoint /
    client.post('/users', data=data, headers=headers)
    response = client.post('/users', data=data, headers=headers)
    data = json.loads(response.data.decode('utf-8'))

    # Fazemos o teste de asserção
    assert response.content_type == mimetype
    assert data['message'] == 'Já existe um(a) usuário com estes dados.'


def test_users_deletar(client):
    """
    **Given** Luiz está acessando a API,
    **When** informa a rota/endpoint `/users/romario`,
    **Then** a api deve deletar o usuário.
    **And** seu conteúdo de envio deve ser
        {
        }
    **And** resposta deve ser
        {
          null
        }
    """
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    # Realiza uma requisição HTTP do tipo post para o endpoint /
    data = """{
                    "name": "romario",
                    "email": "romario@teste.com",
                    "password": "123456"
                }
            """
    client.post('/users', data=data, headers=headers)

    # Realiza uma requisição HTTP do tipo delete para o endpoint /
    response = client.delete('/users/romario')

    data = json.loads(response.data.decode('utf-8'))

    # Fazemos o teste de asserção
    assert response.content_type == mimetype
    assert data == None


def test_users_deletar_user_inexistente(client):
    """
    **Given** Luiz está acessando a API,
    **When** informa a rota/endpoint `/users/romario`, onde romario não existe na base
    **Then** a api deve retornar uma mensagem.
    **And** seu conteúdo de envio deve ser
        {
        }
    **And** resposta deve ser
        {
          "message": "Este(a) Usuário não existe.",
          "resource": "Users"
        }
    """
    # Realiza uma requisição HTTP do tipo delete para o endpoint /
    client.delete('/users/romario')
    response = client.delete('/users/romario')

    data = json.loads(response.data.decode('utf-8'))

    # Fazemos o teste de asserção
    assert data['message'] == 'Este(a) Usuário não existe.'


def test_stats_get_url(client):
    """
    **Given** Luiz está acessando a API,
    **When** informa a rota/endpoint `/stats/1`,
    **Then** a api deve retornar dados da url id 1.
    **And** seu conteúdo de envio deve ser
        {
        }
    **And** resposta deve ser
        {
          "hits": 1,
          "idUrl": 1,
          "short_url": "http://0.0.0.0:5000/867nv",
          "url": "http://www.chaordic.com.br/folksa1423431321321442132133211111124324322332121111111133213212"
        }
    """
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    # Realiza uma requisição HTTP do tipo post para o endpoint /
    data = """{
                    "name": "romario",
                    "email": "romario@teste.com",
                    "password": "123456"
                }
            """
    client.post('/users', data=data, headers=headers)
    data = """{
                    "url": "http://www.chaordic.com.br/folksa1423431321321442132133211111124324322332121111111133213212"
                }
            """

    # Realiza uma requisição HTTP do tipo delete para o endpoint /
    client.post('/users/romario/url', data=data, headers=headers)
    response = client.get('/stats/1')

    data = json.loads(response.data.decode('utf-8'))

    # Fazemos o teste de asserção
    assert response.content_type == mimetype
    assert data['idUrl'] == 1
