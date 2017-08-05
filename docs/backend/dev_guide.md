# Dev Guide

## Admin
To auto-generate `admin.py` file of each app, simply run
```
./manage.py admin_generator 'concierge.<app_name>'
```
This will create the contents of the admin file based on the app models.
If `admin.py` already exists, then the new contents will be appended to the original file.
In any case, do review the newly generated file. Also check for unused imports.
