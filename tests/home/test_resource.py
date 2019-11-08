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

    # Utilizamos a função loads do modulo json para retornar um dict
    # para a váriavel data.
    # Precisamos passar por parâmetro para essa função a resposta
    # retornada pelo servidor, através da váriavel response.data
    # e decodificar para utf-8
    data = json.loads(response.data.decode('utf-8'))

    # Fazemos o teste de asserção
    assert data['hello'] == 'statsGet'