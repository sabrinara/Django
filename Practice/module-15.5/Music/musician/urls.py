from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.all_musician, name="all_musician"),
    path('add/', views.add_musician, name='add_musician'),
]