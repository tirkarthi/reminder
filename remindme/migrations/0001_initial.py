# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=90)),
                ('status', models.IntegerField(choices=[(0, 'pending'), (1, 'sent'), (2, 'failed')], default=0)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
