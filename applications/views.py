from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import ApplicationForm
from .models import Application
from .telegram_service import telegram_notifier

def home(request):
    """Главная страница с формой заявки"""
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            telegram_notifier.notify_new_application(application)
            messages.success(request, 'Ваша заявка успешно отправлена!')
            return redirect('home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ApplicationForm()
    
    return render(request, 'applications/home.html', {
        'form': form
    })

def submit_application(request):
    """AJAX обработчик для отправки заявки"""
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            telegram_notifier.notify_new_application(application)
            return JsonResponse({
                'success': True,
                'message': 'Ваша заявка успешно отправлена!'
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })
    return JsonResponse({'success': False, 'message': 'Неверный метод запроса'})

def api_test(request):
    """Страница для тестирования API"""
    return render(request, 'applications/api_test.html')
