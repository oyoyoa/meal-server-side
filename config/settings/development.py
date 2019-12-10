import os

from .base import *

SECRET_KEY = 'x3att3bk_55o5hpi01th_=g59t3w$x!+fcs5c7@5t)x5osqq)$'
DEBUG = True
JWT_AUTH['JWT_SECRET_KEY'] = SECRET_KEY
ALLOWED_HOSTS = ['localhost', '127.0.0.1', os.environ.get('ADDITIONAL_HOST')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
