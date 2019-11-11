#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os.path import dirname, isfile, join
import pytest
from dotenv import load_dotenv

# Adicione ao path o arquivo .env
_ENV_FILE = join(dirname(__file__), '../.env')

# Carregar load_dotenv
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

# Cria uma fixture que será utilizada no escopo sessão
# a cada execução do comando pytest
@pytest.fixture(scope='session')
def client():
    from apps import create_app
    # Instância função factory
    flask_app = create_app('testing')

    # O Flask fornece um caminho para testar a aplicação utilizando o Werkzeug test Client
    # e manipulando o contexto (configurações)
    testing_client = flask_app.test_client()

    # Antes de executar os testes, é criado um contexto com as configurações da aplicação
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()

@pytest.fixture(scope='function')
def mongo(request, client):

    def fin():
        print('\n[teardown] disconnect from db')

    fin()
