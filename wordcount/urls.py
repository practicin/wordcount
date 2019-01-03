
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('', view.homepage),
    path('count here',view.count),
    path('aboutus', view.aboutus)
]
