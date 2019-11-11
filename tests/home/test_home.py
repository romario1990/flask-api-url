#!/usr/bin/python3
# -*- coding: utf-8 -*-


def test_stats_get_response_200(client):
    # Realiza uma requisição HTTP do tipo get para o endpoint /
    response = client.get('/stats')
    # Verificamos a assertividade do código de resposta da requisição
    # http. Ela deve ser exatamente igual 200 retornando um True para
    # o teste
    assert response.status_code == 200
