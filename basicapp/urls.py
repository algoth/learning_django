from django.contrib import admin
from django.urls import path
from basicapp import views

#TEMPLATE URLs
app_name = 'basicapp'

urlpatterns = [
    # path('others/', views.others, name = 'others'),
    # path('relative/', views.relative, name='relative'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name = 'login')
]