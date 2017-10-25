# Life3.0

### How to run
1. > python3 -m venv venv
2. > source venv/bin/activate
3. > (venv) pip install -r requirements.txt
4. > (venv) python manage.py runserver --settings=life3.config.settings.local
(Instead of --settings, you can set DJANGO_SETTINGS_MODULE=life3.config.settings.local)

### How to build react
1. > cd life3/static/react
2. > npm i
3. > webpack
