from django.urls import path
from . import api_views

app_name = 'api'

urlpatterns = [
    path('applications/', api_views.ApplicationListAPIView.as_view(), name='application-list'),
    path('applications/<int:pk>/', api_views.ApplicationDetailAPIView.as_view(), name='application-detail'),
    path('applications/create/', api_views.ApplicationCreateAPIView.as_view(), name='application-create'),
    path('applications/stats/', api_views.ApplicationStatsAPIView.as_view(), name='application-stats'),
] 