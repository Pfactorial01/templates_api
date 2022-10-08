import os

from config.settings import *  # noqa F401

SECRET_KEY = os.getenv("SECRET_FIRMWARE_KEY", "smH6969!")

LOCA = False

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "193.122.65.123"]

if not LOCA:
    STATIC_ROOT = "/var/www/static"
else:
    STATIC_ROOT = BASE_DIR / "static"

STATIC_URL = "/static-files/"


CELERY_BROKER_URL = "redis://172.17.0.2:6379"
CELERY_RESULT_BACKEND = "redis://172.17.0.2:6379"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"

BASE_URL = "http://localhost:8000"
INVITATION_URL = f"{BASE_URL}/users/invitation"


################################################
# FACT
################################################

FACT_PORT = 5000

FACT_URL = "http://127.0.0.1:{}".format(FACT_PORT)
