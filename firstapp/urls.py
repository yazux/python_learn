from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post, name='post'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^accounts/$', views.accounts, name='accounts'),
    url(r'^accounts/new/$', views.account_new, name='account_new'),
    url(r'^accounts/(?P<pk>[0-9]+)/edit/$', views.account_edit, name='account_edit'),
    url(r'^accounts/(?P<pk>\d+)/remove/$', views.account_remove, name='account_remove'),

    url(r'^transactions/$', views.transactions, name='transactions'),
    url(r'^transactions/(?P<pk>[0-9]+)/edit/$', views.transaction_edit, name='transaction_edit'),
    url(r'^transactions/(?P<pk>\d+)/remove/$', views.transaction_remove, name='transaction_remove'),
]