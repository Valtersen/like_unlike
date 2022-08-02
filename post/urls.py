from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='home'),
    path('like_post/', views.like_post, name='likes')
]