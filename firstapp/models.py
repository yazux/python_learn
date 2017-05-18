# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def __str__(self):
        return self.title


class BankAccount(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.alias.encode('utf-8'))


class TransactionType(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title.encode('utf-8'))


class TransactionIdentity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title.encode('utf-8'))


class Transaction(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    account = models.ForeignKey('BankAccount')
    type = models.ForeignKey('TransactionIdentity')
    subject = models.ForeignKey('TransactionType')
    title = models.CharField(max_length=200)
    sum = models.IntegerField()
    transaction_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title.encode('utf-8'))
