# Eventex

Event System

## TL;DR;

```console
pip install -r requirements-dev.txt
source .wttd/bin/activate
manage runserver
```

## How to develop?

1. Clone the repository;
2. Create a virtualenv with Python 3.8;
3. Activate virtualenv;
4. Install the dependencies;
5. Configure .env;
6. Run tests;
7. Run server;

```console
git clone git@github.com:rafaelbertelli/eventex.git wttd && cd wttd
python -m venv .wttd
source .wttd/bin/activate
python $VIRTUAL_ENV/../manage.py
pip install -r requirements-dev.txt
cp contrib/env-sample .env
```

## How to deploy?

1. Create heroku instance;
2. Send project settings to heroku;
3. Set a secure SECRET_KEY for the instance;
4. Set `DEBUG = FALSE`;
5. Configure e-mail service;
6. Send code to heroku

```console
heroku create <my_instance>
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configure e-mail service
git push heroku master --force
```
