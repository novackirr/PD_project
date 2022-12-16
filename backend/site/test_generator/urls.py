from django.contrib import admin
from django.urls import path, include
from .views import TestGenerate, TestShow, TestFileUploadView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('generate/', TestGenerate.as_view()),
    path('show_test/', TestShow.as_view()),
    path('upload_decision/', TestFileUploadView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)