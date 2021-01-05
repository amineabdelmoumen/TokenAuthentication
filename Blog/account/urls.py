from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register', views.RegisterNewUser, name='register'),
    path('login', obtain_auth_token, name='login')

]
