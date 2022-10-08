import os

from config.settings import *  # noqa F401

SECRET_KEY = os.getenv("SECRET_FIRMWARE_KEY", "smH6969!")

LOCA = True

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "193.122.65.123"]

if not LOCA:
    STATIC_ROOT = "/var/www/static"
else:
    STATIC_ROOT = BASE_DIR / "static"
