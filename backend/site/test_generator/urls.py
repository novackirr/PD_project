from django.contrib import admin
from django.urls import path, include
from .views import TestGenerator

urlpatterns = [
    path('generate/', TestGenerator.as_view())
]