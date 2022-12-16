from django.contrib import admin
from django.urls import path, include
from .views import TestGenerate, TestShow

urlpatterns = [
    path('generate/', TestGenerate.as_view()),
    path('show_test/', TestShow.as_view())
]