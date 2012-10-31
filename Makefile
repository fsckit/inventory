MANAGE=manage.py
VENV=. env/bin/activate;

venv: env/bin/activate
env/bin/activate: requirements.txt
	[ -d env ] || virtualenv env
	${VENV} pip install -r requirements.txt
	touch env/bin/activate

init: venv
	${VENV} echo "no" | python ${MANAGE} syncdb

syncdb: init

update: venv
	${VENV} pip install -U -r requirements.txt

freeze: venv
	${VENV} pip freeze -r requirements.txt > requirements.txt

serve: venv
	${VENV} python ${MANAGE} runserver

test: venv
	${VENV} python ${MANAGE} test

shell: venv
	${VENV} python ${MANAGE} shell

admin: venv
	${VENV} python ${MANAGE} createsuperuser
