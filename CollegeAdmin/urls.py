from django.contrib import admin
from django.urls import path
from CollegeAdmin import views

urlpatterns = [
    path('list', views.TopicListView.as_view()),
    path('list/detail/<int:pk>', views.TopicDetailView.as_view()),
    path('undo-list', views.TopicReviewListView.as_view()),
    path('undo-list/update/<int:pk>', views.ReviewUpdateView.as_view()),
    path('info/<str:pk>', views.AdminInfoUpdateView.as_view()),
    path('score', views.topicScore),
]
