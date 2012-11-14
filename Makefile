MANAGE=manage.py
VENV=. env/bin/activate;

venv: env/bin/activate
env/bin/activate: requirements.txt
	[ -d env ] || virtualenv env
	${VENV} pip install -r requirements.txt
	touch env/bin/activate

init: venv
	${VENV} python ${MANAGE} syncdb --noinput

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

resetdb: venv
	${VENV} python ${MANAGE} reset --noinput `python -c "from app.settings import base; print ' '.join(map(lambda x: x[4:], filter(lambda x: 'app.' in x, base.INSTALLED_APPS)))"`
