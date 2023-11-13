import os
from typing import List
from urllib.parse import urlparse

import sys
from pathlib import Path
from jutil.parse import parse_bool
from dotenv import load_dotenv

load_dotenv(os.path.dirname(__file__) + "/.env")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"

MEDIA_ROOT = Path(os.getenv("MEDIA_ROOT") or BASE_DIR)

LOG_DIR = Path(os.getenv("LOG_DIR") or os.path.join(MEDIA_ROOT, "logs"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = parse_bool(os.environ["DEBUG"])

ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "rest_framework",
    "rest_framework.authtoken",
    "jutil",
    "jstocks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "jutil.middleware.LogExceptionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

db_url = urlparse(os.getenv("DB_URL") or "postgres://dev:dev@localhost:5432/factoring_test")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": db_url.path[1:],
        "USER": db_url.username,
        "PASSWORD": db_url.password,
        "HOST": db_url.hostname,
        "PORT": 5432,
        "CONN_MAX_AGE": 180,
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(BASE_DIR, "jstocks/locale"),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS: List[str] = []

STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder", "django.contrib.staticfiles.finders.AppDirectoriesFinder")


# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "ndebug": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "verbose": {"format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s", "datefmt": "%Y-%m-%d %H:%M:%S"},
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "file": {"level": "DEBUG", "class": "logging.FileHandler", "filename": os.path.join(LOG_DIR, "django.log"), "formatter": "verbose"},
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
        },
    },
    "loggers": {
        "jstocks": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
        },
        "django": {
            "handlers": ["file", "console"],
            "level": "WARNING",
        },
        "jutil": {
            "handlers": ["file", "console"],
            "level": "WARNING",
        },
    },
}
