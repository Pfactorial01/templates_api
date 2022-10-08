import subprocess

from config.settings import *  # noqa F401

DEBUG = False


ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

PUBLIC_IP = subprocess.run(["curl", "ifconfig.me"], capture_output=True)

if PUBLIC_IP.returncode == 0:
    ALLOWED_HOSTS.append(PUBLIC_IP.stdout.decode())

CELERY_BROKER_URL = "redis://localhost:6379"

CELERY_RESULT_BACKEND = "redis://localhost:6379"

CELERY_ACCEPT_CONTENT = ["application/json"]

CELERY_RESULT_SERIALIZER = "json"

CELERY_TASK_SERIALIZER = "json"

BASE_URL = "http://193.122.65.123"

INVITATION_URL = f"{BASE_URL}/users/invitation"
