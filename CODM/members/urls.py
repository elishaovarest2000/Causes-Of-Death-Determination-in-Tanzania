from django.contrib import admin
from. import views
from django.urls import path



urlpatterns = [
    path('', views.Login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
   
]
