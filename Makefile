# Before anything else
THIS_FILE := $(lastword $(MAKEFILE_LIST))
MYSHELL := $(shell echo $$SHELL)
UNAME_S := $(shell uname -s)

.PHONY: run build

help:
	@echo "Available Targets:"
	@cat Makefile | egrep '^([-a-zA-Z]+?):' | sed 's/:\(.*\)//g' | sed 's/^/- /g'

setup-python:
	brew install docker-compose
	pip install flask

setup-aws-cli:
	pip install awscli
	pip install --upgrade --user awsebcli

setup: setup-python setup-aws-cli

delete-node-modules:
	rm -rf node_modules

reset: delete-node-modules setup

run:
	docker build -t guilhermebruzzi/exampleflask .
	docker run -i -t --rm -v "$$PWD/app:/app/app" -p 8080:80 guilhermebruzzi/exampleflask

run_local:
	PORT=5000 python app/main.py

logs:
	eb logs example-flask-dev

deploy:
	eb deploy example-flask-dev
