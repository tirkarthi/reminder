from celery.decorators import task
from django.core.mail import send_mail


@task()
def send_reminder_mail(email, message, id):
    from .models import Reminder

    subject = 'Subject : ' + message
    message = 'body : ' + message
    recipients = [email]
    reminder = Reminder.objects.get(id=id)
    try:
        send_mail(subject, message, 'tir.karthi@gmail.com', recipients)
        reminder.status = Reminder.STATE_SENT
    except e:
        reminder.status = Reminder.STATE_FAILED
    finally:
        reminder.save()
