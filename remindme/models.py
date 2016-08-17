import datetime
from django.utils import timezone
from django.db import models
from .tasks import send_reminder_mail

# Create your models here.
class Reminder(models.Model):

    STATE_PENDING = 0
    STATE_SENT    = 1
    STATE_FAILED  = 2
    
    STATE_CHOICES = (
        (STATE_PENDING, "pending"),
        (STATE_SENT, "sent"),
        (STATE_FAILED, "failed"),
    )
    
    email = models.EmailField()
    message = models.CharField(max_length=90)
    status  = models.IntegerField(choices=STATE_CHOICES, default=0)
    time  = models.DateTimeField()

    def save(self, *args, **kwargs):
        obj = super().save(*args, **kwargs)
        send_reminder_mail.apply_async((self.email, self.message, self.id))
