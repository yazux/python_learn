from django import forms
from .models import Post
from .models import BankAccount
from .models import Transaction

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class AccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ('alias', 'title', 'description')

class DateInput(forms.DateInput):
    input_type = 'date'

class TransactionForm(BaseForm):
    class Meta:
        model = Transaction
        fields = ('account', 'type', 'subject', 'title', 'sum', 'transaction_date')
        widgets = {
            'transaction_date': DateInput()
        }
