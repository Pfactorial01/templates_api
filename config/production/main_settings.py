import subprocess

from config.settings import *  # noqa F401

DEBUG = False

PRODUCTION = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

PUBLIC_IP = subprocess.run(["curl", "ifconfig.me"], capture_output=True)

if PUBLIC_IP.returncode == 0:
    ALLOWED_HOSTS.append(PUBLIC_IP.stdout.decode())
    BASE_URL = f"http://{PUBLIC_IP.stdout.decode()}"
else:
    BASE_URL = "http://127.0.0.1"

CELERY_BROKER_URL = "redis://172.20.0.10:6379"

CELERY_RESULT_BACKEND = CELERY_BROKER_URL

CELERY_ACCEPT_CONTENT = ["application/json"]

CELERY_RESULT_SERIALIZER = "json"

CELERY_TASK_SERIALIZER = "json"

INVITATION_URL = f"{BASE_URL}/users/invitation"

#########################
# Externals
#########################

FACT_PORT = 8889

FACT_URL = "http://193.122.65.123:{}".format(FACT_PORT)

EMUX_PORT = 8999

EMUX_URL = "http://193.122.65.123:{}/fapei".format(EMUX_PORT)
