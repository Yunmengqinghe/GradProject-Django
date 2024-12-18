from django.contrib import admin
from django.urls import path
from Mentor import views

urlpatterns = [
    path('home', views.TopicListView.as_view()),
    path('new', views.TopicInfoCreateView.as_view()),
]
