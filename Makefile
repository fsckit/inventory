init:
	[ -d env ] || virtualenv env
	. env/bin/activate
	pip install -r requirements.txt
	python manage.py syncdb

update:
	pip install -U -r requirements.txt

freeze:
	pip freeze -r requirements.txt > requirements.txt

serve:
	python manage.py runserver

test:
	python manage.py test
