
# News Focus REST API

Query news from Google. Provides a JSON response to the user.
Uses GNews Python library to collect news. 
Makes use of Flask library to create RESTful APIs.


## Acknowledgements
- [GNews](https://github.com/ranahaani/GNews)

 


## Pre-requisites
    1. Flask
    2. Flask-SQLAlchemy
    3. Flask Marshmallow
    4. Marshmallow SQLAlchemy
    5. GNews
    

## Installation
    pip install flask
    pip install flask-sqlalchemy
    pip install flask-marshmallow
    pip install marshmallow-sqlalchemy
    pip install gnews
## Configuration Details
You need to create a ```config.py``` file in the ```news_focus_backend/``` dir 
and write the following code:

```
# Define the application directory
import os

# Statement for enabling the development environment
from sqlalchemy.pool import QueuePool, NullPool

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
#
SQLALCHEMY_ENGINE_OPTIONS = {
    'poolclass': NullPool,
}

DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores to handle
# incoming requests using one and performing background
# operation using the other.
THREADS_PER_PAGE = 2

# Enable protection against *Cross-Site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
# This secret key can be generated in python terminal as follows:
# import uuid
# uuid.uuid4().hex
CSRF_SESSION_KEY = "SECRET_KEY"

# Secret key for signing cookies
# This secret key can be generated in python terminal as follows:
# import uuid
# uuid.uuid4().hex
SECRET_KEY = "SECRET_KEY"
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/sohaibrahman64/news_focus_backend.git
```

Go to the project directory

```bash
  cd news_focus_backend
```

Install dependencies

```bash
  pip install flask
  pip install flask-sqlalchemy
  pip install flask-marshmallow
  pip install marshmallow-sqlalchemy
  pip install gnews
  pip install newspaper3k
```

Start the server

```bash
  python run.py
```

