C_NAME ?= application_api

up:
	docker compose down && docker compose up --build -d

down:
	docker compose down

logs:
	docker logs -f --tail 100 $(C_NAME)

bash:
	docker exec -it $(C_NAME) bash
