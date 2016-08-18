
from django.utils import timezone
from rest_framework import serializers
from .models import *


class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ('id', 'message', 'status', 'email', 'time')

    def validate_time(self, value):
        """
        Check that the time is greater than the current time
        """

        if value < timezone.now():
            raise serializers.ValidationError(
                "Time should be greater than the current time")
        return value
