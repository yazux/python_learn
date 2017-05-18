from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import datetime
from .models import Post
from .models import BankAccount
from .models import Transaction

from .forms import PostForm
from .forms import AccountForm
from .forms import TransactionForm

from django.shortcuts import redirect


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/posts.html', {'posts': posts})


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'app/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'app/post_edit.html', {'form': form})

def accounts(request):
    if request.user.is_authenticated:
        accounts = BankAccount.objects.filter(user=request.user).order_by('created_date')
        return render(request, "app/bank_account/accounts.html", {'accounts': accounts})
    else:
        return redirect('index')


def account_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AccountForm(request.POST)
            if form.is_valid():
                account = form.save(commit=False)
                account.user = request.user
                account.created_date = timezone.now()
                account.save()
                return redirect('accounts')
        else:
            form = AccountForm()
        return render(request, 'app/bank_account/account_edit.html', {'form': form})
    else:
        return redirect('index')



def account_edit(request, pk):
    if request.user.is_authenticated:
        account = get_object_or_404(BankAccount, pk=pk)
        if request.method == "POST":
            form = AccountForm(request.POST, instance=account)
            if form.is_valid():
                account = form.save(commit=False)
                account.author = request.user
                account.published_date = timezone.now()
                account.save()
                return redirect('accounts')
        else:
            form = AccountForm(instance=account)
        return render(request, 'app/bank_account/account_edit.html', {'form': form})
    else:
        return redirect('index')

def account_remove(request, pk):
    if request.user.is_authenticated:
        account = get_object_or_404(BankAccount, pk=pk)
        account.delete()
        return redirect('accounts')
    else:
        return redirect('index')


def transactions(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = TransactionForm(request.POST)
            transaction = form.save(commit=False)
            transaction.published_date = timezone.now()
            transaction.user = request.user
            transaction.save()
            return redirect('transactions')
        else:
            form = TransactionForm()

            if request.method == 'GET' and 'date' in request.GET:
                requestDate = datetime.strptime(request.GET['date'], '%m.%Y')
            else:
                requestDate = datetime.today()

            # get current user transactions by current month
            transactions = Transaction.objects.filter(
                transaction_date__month=requestDate.month,
                transaction_date__year=requestDate.year,
                user=request.user
            ).order_by('-transaction_date')

            # get current user transactions by all time
            allTransactions = Transaction.objects.filter(user=request.user).order_by('-transaction_date')

            # get current user bank accounts
            accounts = BankAccount.objects.filter(user=request.user).order_by('created_date')

            # convert object BankAccount to list
            new_accounts = []
            for account in accounts:
                new_accounts.append((account.id, account.alias))

            # change form field "account" to current user bank accounts
            form.fields["account"].choices = new_accounts

            # calculate transactions amount by bank accounts
            accountsSum = {}
            i = 0
            for account in accounts:
                accountsSum[i] = {
                    'name': str(account.alias.encode('utf-8')),
                    'sum': 0
                }

                for transaction in allTransactions:
                    if str(transaction.account.alias.encode('utf-8')) == str(account.alias.encode('utf-8')):
                        if transaction.type.title == 'Receiving':
                            accountsSum[i]['sum'] = accountsSum[i]['sum'] + transaction.sum
                        else:
                            accountsSum[i]['sum'] = accountsSum[i]['sum'] - transaction.sum

                i = i + 1



            return render(
                request,
                "app/transactions/transactions.html",
                {'transactions': transactions, 'form': form, 'accounts': accountsSum}
            )
    else:
        return redirect('index')




def transaction_edit(request, pk):
    if request.user.is_authenticated:
        transaction = get_object_or_404(Transaction, pk=pk)
        if request.method == "POST":
            form = TransactionForm(request.POST, instance=transaction)
            if form.is_valid():
                transaction = form.save(commit=False)
                transaction.published_date = timezone.now()
                transaction.user = request.user
                transaction.save()
                return redirect('transactions')
        else:
            form = TransactionForm(instance=transaction)
        return render(request, 'app/transactions/transaction_edit.html', {'form': form})
    else:
        return redirect('index')

def transaction_remove(request, pk):
    if request.user.is_authenticated:
        transaction = get_object_or_404(Transaction, pk=pk)
        transaction.delete()
        return redirect('transactions')
    else:
        return redirect('index')