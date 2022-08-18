.PHONY: up
up:
	docker-compose up

.PHONY: down
down:
	docker-compose down

.PHONY: in
in:
	docker exec -ti stewards-backend /bin/bash