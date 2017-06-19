# Dev Guide

## Admin
To auto-generate `admin.py` file of each app, simply use [django-admin-generator](https://github.com/WoLpH/django-admin-generator). Invoke it in the following way:
```
./manage.py admin_generator 'concierge.<app_name>' >> concierge/<app_name>/admin.py
```
Though do remove the `prepopulated_fields` line from admin.py (if present)

## Fixtures
To load all fixtures, run the shell script `load_fixtures.sh`

