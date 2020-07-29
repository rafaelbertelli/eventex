# Eventex

Event System

## TL;DR;

```console
source .wttd/Scripts/activate
manage collectstatic            # only when neccessary
manage runserver
```

## How to develop?

1. Clone the repository;
2. Create a virtualenv with Python 3.8;
3. Activate virtualenv;
4. Run server; <small>**It's recommended to create an alias for this command</small>

```console
git clone git@github.com:rafaelbertelli/eventex.git wttd && cd wttd
python -m venv .wttd
source .wttd/Scripts/activate
python $VIRTUAL_ENV/../manage.py
```
