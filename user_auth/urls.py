from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.create_user),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]