from django.conf.urls import include, url
from rest_framework import routers

from .views import *


urlpatterns = [
        url(r'api/reminders/$', ReminderViewSet.as_view()),
        url(r'api/reminders/(?P<pk>[0-9]+)$', ReminderViewSetDetail.as_view()),
]
