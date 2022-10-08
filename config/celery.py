from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


app.conf.beat_schedule = {
    "update_threat_intelligence": {
        "task": "update_threat_intelligence",
        "schedule": 300.0,  # Every 5 minutes
    },
    "notify_user_for_comparison": {
        "task": "notify_user_for_comparison",
        "schedule": 300.0,  # Every 5 minutes
    },
}
