from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_application, name='submit_application'),
    path('api-test/', views.api_test, name='api_test'),
] 