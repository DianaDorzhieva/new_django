from celery import shared_task
from django.core.mail import send_mail
from config import settings
from course.models import Course


@shared_task
def mail_update_course(course_id):
    course = Course.objects.get(pk=course_id)
    recipient_list = course.subscriptions_set.values_list('user_email', flat=True)
    send_mail(
        subject='Обновление курса',
        message=f'{course.name} обновился, посмотрите что теперь нового',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list
    )
