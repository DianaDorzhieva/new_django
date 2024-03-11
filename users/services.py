import json
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def chek_3_tasc():
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.DAYS,
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name='Chek users',
        task='users.task.chek_user',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
