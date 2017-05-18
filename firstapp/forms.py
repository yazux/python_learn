from django import forms
from .models import Post
from .models import BankAccount
from .models import Transaction


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class AccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ('alias', 'title', 'description')

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'type', 'subject', 'title', 'sum', 'transaction_date')