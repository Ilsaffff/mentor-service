migrate:
	python manage.py makemigrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser

freeze:
	pip freeze > requierements

shell:
	python manage.py shell