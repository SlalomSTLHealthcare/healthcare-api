"""
Django settings for healthcare api project.
Dan Borstelmann -- July 2, 2018

Production settings file to select proper environment variables.
"""

import os
from django.core.exceptions import ImproperlyConfigured
import dj_database_url


def get_env_variable(env_var, optional=False):
    """Get the environment variable or return exception"""
    try:
        return os.environ[env_var]
    except KeyError:
        if optional:
            return ''
        else:
            error = "environment variable '{ev}' not found.".format(ev=env_var)
            raise ImproperlyConfigured(error)


DEBUG = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSRF_COOKIE_SECURE = True
SECRET_KEY = 'HEALTHSTLX'
ALLOWED_HOSTS = ["localhost", ".herokuapp.com"]


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.views.decorators.csrf',
    'django.db.models.signals',
    'django.dispatch',
    'api',
    'authentication',
    'corsheaders'
)

MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False
ROOT_URLCONF = 'healthstlx.urls'

WSGI_APPLICATION = 'healthstlx.wsgi.application'

if 'HEALTHSTLX_LOCAL_NAME' not in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(get_env_variable("DATABASE_URL"))
    }
else:
    DATABASES = {
        'default': {
            'HOST': 'localhost',
            'PORT': '5432',
            'NAME': get_env_variable("HEALTHSTLX_LOCAL_NAME"),
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': get_env_variable("HEALTHSTLX_LOCAL_USERNAME"),
            'PASSWORD': get_env_variable("HEALTHSTLX_LOCAL_PASSWORD"),
        },
    }

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
