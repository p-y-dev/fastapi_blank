C_NAME ?= app_api
MIGR_NAME ?= migration

up:
	docker compose down && docker compose up --build --remove-orphans -d

down:
	docker compose down

migration:
	docker exec $(C_NAME) alembic revision --autogenerate -m "$(MIGR_NAME)"

migrate:
	docker exec $(C_NAME) alembic upgrade head

check:
	docker exec $(C_NAME) flake8
	docker exec $(C_NAME) mypy .
	docker exec $(C_NAME) black --check .
	docker exec $(C_NAME) pytest . -n auto # -rP

logs:
	docker logs -f --tail 100 $(C_NAME)

bash:
	docker exec -it $(C_NAME) bash

tests:
	docker exec $(C_NAME) pytest . -n auto # -rP
