init:
	[ -d env ] || virtualenv env
	. env/bin/activate
	pip install -r requirements.txt

update:
	pip install -U -r requirements.txt

serve:
	python manage.py runserver

test:
	python manage.py test
