# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-15 23:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20180415_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippets',
            name='file_name',
        ),
    ]
