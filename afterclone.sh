docker compose -f docker-compose-dev.yaml up -d --build

cd AvtoInfo

poetry run python3 manage.py migrate

poetry run python3 manage.py loaddata fixtures/users/users.json

poetry run python3 manage.py loaddata fixtures/cars/cars.json

poetry run python3 manage.py loaddata fixtures/cars/comments.json

poetry run python3 manage.py runserver
