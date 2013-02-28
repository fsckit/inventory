web: python myapp/manage.py collectstatic --noinput; gunicorn -k gevent -k socketio.sgunicorn.GeventSocketIOWorker scripts.wsgi
