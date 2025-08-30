from .base import *
from urllib.parse import urlparse, parse_qsl

DEBUG = os.environ.get("DJANGO_DEBUG", "")  != "False"

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': tmpPostgres.path.replace('/', ''),
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
        'OPTIONS': dict(parse_qsl(tmpPostgres.query)),
    }
}
