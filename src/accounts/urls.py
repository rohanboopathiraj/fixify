from . import views
from django.urls import path

urlpatterns = [
    path('users/', views.FixifyUserListAPIView.as_view(),
         name='list-all-account'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register')

]
