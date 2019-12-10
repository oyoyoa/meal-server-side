# import django_heroku
import dj_database_url
import django_heroku

from .base import *


DEBUG = False
ALLOWED_HOSTS = ['*']

SECRET_KEY = '@(o)5pq(3(fj#^s_n!vik&e0o@+6ezbjpbf^8(gst@(f+z(rjb'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# django_heroku.settings(locals())
DATABASES = {
    'default': dj_database_url.config()
}
django_heroku.settings(locals())
