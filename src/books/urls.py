from django.urls import re_path as url

from . import views

app_name = 'books'

urlpatterns = [
    url(r'^/$', views.login, name='login')
]
