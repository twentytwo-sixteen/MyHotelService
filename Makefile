.PHONY: up down stop-local-postgres

# Остановить локальный PostgreSQL, если он слушает 5432
stop-local-postgres:
	@echo "Проверка, кто слушает порт 5432..."
	@if sudo lsof -i :5432 | grep LISTEN; then \
		echo "Обнаружен процесс на порту 5432. Завершаем..."; \
		sudo systemctl stop postgresql || sudo kill -9 $$(sudo lsof -ti :5432); \
	else \
		echo "Порт 5432 свободен."; \
	fi

# Поднять сервисы (предварительно остановив локальный PostgreSQL)
up: stop-local-postgres
	docker-compose up -d

# Остановить сервисы и подчистить сеть
down:
	docker-compose down && docker network prune --force
