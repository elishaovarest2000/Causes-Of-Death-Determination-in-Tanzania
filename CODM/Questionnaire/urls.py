from django.urls import path
from. import views


urlpatterns = [
    path('mahojiano/', views.mahojiano , name='mahojiano'),
    path('Questionnaire/', views.questionnaire_view, name='Questionnaire'),
    path('Questionnaire/<str:message>/', views.questionnaire_view, name='Questionnaire'),
] 

