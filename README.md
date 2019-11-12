# flask-api-url

Uma api com Flask Framework, MongoDB de encurtamento de url

## Commands

```shell
make clean
       Preparar ambiente de desenvolvimento, use apenas uma vez
make clean-build
       Limpar todos os diretórios de construção
make isort
       Execute o comando isort em recursos de desenvolvimento
make lint
       run lint
make test
       run testes
make run
       Execute o aplicativo da web flask-api-url
```
## Inicio

Utilizar versão do python 3.5

OBS: executar com virtualenv ativo

Instalar dependências:

Install pacotes basicos `pip install -r requirements/base.txt`

Install pacotes desenvolcimento `pip install -r requirements/dev.txt`

Install pacotes prod `pip install -r requirements/prod.txt`

Install pacotes prod `pip install -r requirements/test.txt`


OBS. Caso queira pode customizar algumas variáveis de ambiente editando o arquivo `.env`.


## Crie MongoDB - Pré-requisito para aplicação

```shell
$ docker run --name mongo-latest -p 27017:27017 -d mongo
```

## Excute a aplicação de executar

```shell
$ make run
```

