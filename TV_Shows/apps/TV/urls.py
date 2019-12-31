from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows/new$', views.create),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^submitCreate$', views.createProcess),
    url(r'^shows/(?P<id>\d+)$', views.show),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit),
    url(r'^editProcess/(?P<id>\d+)$', views.editProcess),
]