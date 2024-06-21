"""
Django settings for weather_forecast project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import read_dotenv
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

if Path.exists(BASE_DIR.joinpath('.env')):
    read_dotenv(BASE_DIR.joinpath('.env'))
else:
    raise ImproperlyConfigured('.env file not found.')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qw)iy9f618s9_s3sf2-)o9v)67&f1blikt)!s8l(0hm8-s6^$z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv('DEBUG'))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'weatherapp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'weather_forecast.urls'

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
        },
    },
]

WSGI_APPLICATION = 'weather_forecast.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / os.getenv('DATABASE'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOG_DIR = BASE_DIR.parent
LOG_FILE = os.getenv('LOG_FILE_NAME', 'weather.log')


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "regular": {
            "format": "%(asctime)s | %(module)s / %(funcName)s / %(levelname)s ==> %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S"
        },
    },
    "handlers": {
        "file": {
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "class": "logging.FileHandler",
            "formatter": "regular",
            "filename": LOG_DIR / LOG_FILE,
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "regular",  # Ensure the console handler uses a formatter
            "level": "DEBUG"
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "default": {
            "handlers": ["console", "file"],
            "level": "DEBUG",  # Set a level for the 'default' logger
            "propagate": True,
        },
    },
}

OPEN_WEATHERMAP_API_KEY=os.getenv('OPEN_WEATHERMAP_API_KEY')
OPEN_WEATHERMAP_API_BASE=os.getenv('OPEN_WEATHERMAP_API_BASE')
CACHE_TIME_IN_MINUTES = int(os.getenv('CACHE_TIME_IN_MINUTES', 10))