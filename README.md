# Life3.0

### How to run server
1. python3 -m venv venv
2. source venv/bin/activate
3. (venv) pip install -r requirements.txt
4. (venv) export PYTHONPATH={your project root path}
5. (venv) export DJANGO_SETTINGS_MODULE=life3.config.settings.local
5. (venv) python manage.py makemigrations app
6. (venv) python manage.py migrate
7. (venv) python manage.py runserver

### How to build react
1. cd life3/static/react
2. npm i
3. webpack

###To see how does SQL work, try like this:
(venv) python manage.py sqlmigrate app 0001_initial
