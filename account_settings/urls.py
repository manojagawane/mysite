# coding: utf-8
from django.conf.urls import include, url
from account_settings import views

urlpatterns = [
    url(r'^$', views.settings, name='settings'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^emails/$', views.emails, name='emails'),
    url(r'^picture/$', views.picture, name='picture'),
    url(r'^password/$', views.password, name='password'),
    
    url(r'^upload_picture/$', views.upload_picture, name='upload_picture'),
    url(r'^save_uploaded_picture/$', views.save_uploaded_picture, name='save_uploaded_picture'),
]
