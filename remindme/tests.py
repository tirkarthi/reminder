from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from time import sleep
import datetime

from .models import Reminder

class AccountTests(APITestCase):
    def test_create_reminder(self):
        """
        Ensure we can create a new Reminder object.
        """
        data = {'email' : 'xtre@yopmail.com', 'message' : 'Buy Milk', 'time' : timezone.now() + datetime.timedelta(seconds=30) }
        url = reverse('reminder-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reminder.objects.count(), 1)
        self.assertEqual(Reminder.objects.get().message, 'Buy Milk')

    def test_create_reminder(self):
        """
        Ensure we can delete a new Reminder object.
        """
        data = {'email' : 'xtre@yopmail.com', 'message' : 'Buy Milk', 'time' : timezone.now() + datetime.timedelta(seconds=30) }
        url = reverse('reminder-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        id = response.data['id']
        url = reverse('reminder-detail', kwargs={'pk': id})
        response = self.client.delete(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_validate_time(self):
        """
        Ensure we can create a new Reminder object with valid email
        """
        data = {'email' : 'xtre@yopmail,,com', 'message' : 'Buy Milk', 'time' : timezone.now() + datetime.timedelta(seconds=30) }
        url = reverse('reminder-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_time(self):
        """
        Ensure we can create a new Reminder object with time greater than the current time
        """
        data = {'email' : 'xtre@yopmail.com', 'message' : 'Buy Milk', 'time' : timezone.now() - datetime.timedelta(seconds=30) }
        url = reverse('reminder-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_message(self):
        """
        Ensure we have a message
        """
        data = {'email' : 'xtre@yopmail,,com', 'message': '', 'time' : timezone.now() + datetime.timedelta(seconds=30) }
        url = reverse('reminder-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
