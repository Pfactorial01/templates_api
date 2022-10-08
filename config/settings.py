import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-pifc@mft$yre8q1uqfns*$djza7nh2c9utm2$!=0^%p^0100n5"

DEBUG = True

PRODUCTION = False

API_ENABLED = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users",
    "firmware",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "notifications",
]

if DEBUG:
    INSTALLED_APPS.append("drf_yasg")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # 'DIRS': [os.path.join(os.path.dirname(__file__), 'templates'),],
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

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/api/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

LOGIN_URL = "/api/login/"

OTX_API_KEY = os.getenv("OTX_API_KEY")


##################################################
# Rest Framework Settings
##################################################

PAGINATION_CLASS = "rest_framework.pagination.PageNumberPagination"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": PAGINATION_CLASS,
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "PAGE_SIZE": 30,
}

SIMPLE_JWT = {"ACCESS_TOKEN_LIFETIME": timedelta(hours=1)}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"},
    }
}

CORS_ALLOW_ALL_ORIGINS = bool(1)

##################################################
# CELERY STUFF
##################################################

CELERY_BROKER_URL = "redis://172.17.0.2:6379"

CELERY_RESULT_BACKEND = "redis://172.17.0.2:6379"

CELERY_ACCEPT_CONTENT = ["application/json"]

CELERY_TASK_SERIALIZER = "json"

CELERY_RESULT_SERIALIZER = "json"

CELERY_TIMEZONE = "GMT"

##################################################
# LOGGING
##################################################

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
}

################################################
# FACT
################################################

FACT_PORT = 8887

FACT_URL = "http://193.122.65.12:{}".format(FACT_PORT)

################################################
# EMUX
################################################

EMUX_PORT = 8886

EMUX_URL = "http://193.122.65.12:{}".format(EMUX_PORT)

##################################################
# RADARE
##################################################
RADARE_PORT = "8888"

RADARE_URL = "http://193.122.65.123"


################################################
# EMAIL
################################################

EMAIL_HOST = os.getenv("EMAIL_HOST")

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")

EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

EMAIL_PORT = 587

EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = "TFAP <no-reply@tfap.org>"  # TODO: change
