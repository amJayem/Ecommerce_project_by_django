from django.contrib import admin
from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.shop_home, name='home'),
    
]