from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.loginAttempt),
    url(r'^dashboard$', views.dashboard),
    url(r'^userQuotes/(?P<userId>\d+)$', views.userQuotes),
    url(r'^createQuote$', views.createQuote),
    url(r'^edit/(?P<quoteId>\d+)$', views.editQuotes),
    url(r'^update/(?P<quoteId>\d+)$', views.updateQuotes),
    url(r'^delete/(?P<quoteId>\d+)$', views.delete),
    url(r'^addFav/(?P<quoteId>\d+)$', views.addFav),
    url(r'^removeFav/(?P<quoteId>\d+)$', views.removeFav),
    url(r'^logout$', views.logout),
]