init:
	[ -d bin ] || virtualenv .
	. bin/activate
	pip install -r requirements.txt

update:
	pip install -U -r requirements.txt

serve:

test:
