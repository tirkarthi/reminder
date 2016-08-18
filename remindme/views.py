from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.http import Http404

from .serializers import *
from .models import *


class ReminderViewSet(generics.ListCreateAPIView):
    serializer_class = ReminderSerializer

    def post(self, request, format=None):
        '''
        email - A valid email ID
        message - A valid message
        time - Time for the mail to be sent of the format "YYYY-MM-DDTHH:MM:SS"

        Format : http POST <host>/api/reminders/ email=<email> message=<message> time=<time>
        Example : http POST :9000/api/reminders/ email="tir.karthi@gmail.com" message="Notify me" time="2016-08-18T04:53:50"
        '''

        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Reminder.objects.all().order_by('-time')
        return queryset


class ReminderViewSetDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReminderSerializer

    def get_object(self, pk):
        try:
            return Reminder.objects.get(id=pk)
        except Reminder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        message - The message to be sent
        status - The status of the reminder
        email - The email ID for the reminder
        time - Time for the reminder mail to be sent

        format : http <host>/api/reminders/<id>
        Example : http :9000/api/reminders/24
        '''

        Reminder = self.get_object(pk)
        serializer = ReminderSerializer(Reminder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        '''
        Edit the reminder

        format : http <host>/api/reminders/<id>
        Example : http :9000/api/reminders/24
        '''

        reminder = self.get_object(pk)
        serializer = ReminderSerializer(reminder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        '''
        Delete the reminder

        format : http <host>/api/reminders/<id>
        Example : http :9000/api/reminders/24
        '''

        reminder = self.get_object(pk)
        reminder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
