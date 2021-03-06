# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
