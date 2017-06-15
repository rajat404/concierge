web: uwsgi uwsgi.ini
worker: celery -A concierge worker -l info --concurrency=2 -B
