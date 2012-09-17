MANAGE=manage.py
init:
	[ -d env ] || virtualenv env
	. env/bin/activate
	pip install -r requirements.txt
	python ${MANAGE} syncdb
	echo "Type . env/bin/activate to enter virutal environment"

update:
	pip install -U -r requirements.txt

freeze:
	pip freeze -r requirements.txt > requirements.txt

serve:
	python ${MANAGE} runserver

test:
	python ${MANAGE} test
