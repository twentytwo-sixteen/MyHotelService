- Для запуска контейнеров используйте команду
```make up```
-Для остановки
```make down```
-Для коммита миграций бд использовать команду
```docker-compose exec app alembic revision --autogenerate -m "Comment"```
-Для применения изменений
```docker-compose exec app alembic upgrade head```
-Cтек:
PosgreSQL, FastAPI, Python, Docker, Docker Compose, Poetry, flake-8..
-Настроен CI с линтерами и тестами.
