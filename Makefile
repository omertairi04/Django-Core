.PHONY: install

install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python3 -m core.manage migrate

.PHONY: makemigrations
migrations:
	poetry run python3 -m core.manage makemigrations

.PHONY: runserver
run-server:
	poetry run python3 -m core.manage runserver

.PHONY: superuser
superuser:
	poetry run python3 -m core.manage createsuperuser

.PHONY: update
update: install migrate;



