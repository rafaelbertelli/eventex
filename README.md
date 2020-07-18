# Eventex

Event System

## How to develop?

1. Clone the repository.
2. Create a virtualenv with Python 3.6
3. Activate virtualenv.
4. Install the dependencies.
5. Configure the instance with .env
6. Run the tests.

```console
git clone git@github.com:rfdeoliveira/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```