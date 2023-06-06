from django.urls import path
from . import views

urlpatterns = [
    path('messages/<str:owner>/', views.messages),
    path('profile/<str:owner>/', views.profile),
    path('response/', views.response),
]