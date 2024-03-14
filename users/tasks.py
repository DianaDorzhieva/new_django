from datetime import timezone
from celery import shared_task
from dateutil import relativedelta

from users.models import User


@shared_task
def chek_user():
    now = timezone.now()
    month_ago = now - relativedelta(months=1)
    users_list = User.objects.filter(is_active=True, date_joined=month_ago)
    for user in users_list:
        user.is_active = False
        user.save()
