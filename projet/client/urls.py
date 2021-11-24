from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/<str:pk>', views.list_client, name='client'),
]
