from django.contrib import admin
from django.urls import path

from myapp.views import *

urlpatterns = [
    path('', GeneratePdf.as_view()),
]