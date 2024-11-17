from . import views
from django.urls import path

urlpatterns = [
    path('users/login', views.FixifyUserListCreateAPIView.as_view(),
         name='account-login'),
    path('users/', views.FixifyUserListCreateAPIView.as_view(),
         name='account-registration')
]
