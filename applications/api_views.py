from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import Application
from .serializers import ApplicationSerializer, ApplicationListSerializer

class ApplicationListAPIView(generics.ListAPIView):
    """
    GET запрос для получения списка всех заявок
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationListSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['-created_at']

class ApplicationDetailAPIView(generics.RetrieveAPIView):
    """
    GET запрос для получения детальной информации о заявке
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

class ApplicationCreateAPIView(generics.CreateAPIView):
    """
    POST запрос для создания новой заявки
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApplicationStatsAPIView(generics.GenericAPIView):
    """
    GET запрос для получения статистики заявок
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        total_applications = Application.objects.count()
        today_applications = Application.objects.filter(
            created_at__date=timezone.now().date()
        ).count()
        
        # Статистика по дням за последние 7 дней
        weekly_stats = []
        for i in range(7):
            date = timezone.now().date() - timedelta(days=i)
            count = Application.objects.filter(
                created_at__date=date
            ).count()
            weekly_stats.append({
                'date': date.strftime('%Y-%m-%d'),
                'count': count
            })
        
        return Response({
            'total_applications': total_applications,
            'today_applications': today_applications,
            'weekly_stats': weekly_stats
        }) 