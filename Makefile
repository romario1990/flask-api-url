.PHONY: help clean test clean-build isort run

.DEFAULT: help

help:
	@echo "make clean"
	@echo "       Preparar ambiente de desenvolvimento, use apenas uma vez"
	@echo "make clean-build"
	@echo "       Limpar todos os diretórios de construção"
	@echo "make isort"
	@echo "       Execute o comando isort em recursos de desenvolvimento"
	@echo "make lint"
	@echo "       run lint"
	@echo "make test"
	@echo "       run testes"
	@echo "make run"
	@echo "       Execute o aplicativo da web flask-api-url"

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pyc|.DS_Store$$" | xargs rm -rf

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

lint:
	make clean
	flake8

test:
	make lint
	pytest --verbose --color=yes

run:
	make test
	python3 application.py
