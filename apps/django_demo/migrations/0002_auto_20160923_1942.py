# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 19:42
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('django_demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='pokes',
            managers=[
                ('pokeMgr', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='pokes',
            name='pokes',
        ),
    ]