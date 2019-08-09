build:
	docker-compose build

up-daemon:
	docker-compose up -d

up:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -ti my_nginx /bin/sh

shell-web:
	docker exec -ti my_app /bin/sh

shell-db:
	docker exec -ti my_db /bin/sh

log-nginx:
	docker-compose logs nginx

log-web:
	docker-compose logs web

log-db:
	docker-compose logs db

collectstatic:
	docker exec my_app /bin/sh -c "python manage.py collectstatic --noinput"