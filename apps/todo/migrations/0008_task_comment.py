# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20170604_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
