# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post
from .models import BankAccount
from .models import TransactionType
from .models import TransactionIdentity
from .models import Transaction

admin.site.register(Post)
admin.site.register(BankAccount)
admin.site.register(TransactionType)
admin.site.register(TransactionIdentity)
admin.site.register(Transaction)