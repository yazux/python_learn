# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 04:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_bankaccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='user',
        ),
        migrations.DeleteModel(
            name='BankAccount',
        ),
    ]
