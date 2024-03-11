from datetime import datetime
from celery import shared_task
from django.core.mail import send_mail
from config import settings
from course.models import Subscriptions
from users.models import User


@shared_task
def mail_update_course(course_id):
    subs = Subscriptions.objects.filter(course_id=course_id)
    for sub in subs:
        send_mail(
            subject='Обновление курса',
            message=f'{sub.course.name} обновился, посмотрите что теперь нового',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.user.email]
        )

@shared_task
def chek_user():
    now = datetime.now()
    user_all = User.objects.filter(is_active=True)
    for user in user_all:
        if now - user.last_login >= 30:
            user.is_active = False
