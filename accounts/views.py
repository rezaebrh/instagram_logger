from django.shortcuts import render, redirect
from .models import InstagramAccount, Log
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .tasks import long_running_task
from .models import RetrievedAccount

def create_instagram_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        instagram_account = InstagramAccount(username=username, password=password)
        instagram_account.save()
        return redirect('account_list')
    return render(request, 'create_instagram_account.html')


def log_message(request):
    if request.method == 'POST':
        account_id = request.POST.get('account_id')
        message = request.POST.get('log_message')
        account = InstagramAccount.objects.get(id=account_id)
        log = Log(instagram_account=account, log_message=message)
        log.save()
        return redirect('log_list')
    accounts = InstagramAccount.objects.all()
    return render(request, 'log_message.html', {'accounts': accounts})


def account_list(request):
    accounts = InstagramAccount.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})


def log_list(request):
    logs = Log.objects.all()
    return render(request, 'log_list.html', {'logs': logs})

def home(request):
    return render(request, 'home.html')


def start_task(request):
    if request.method == 'POST':
        # Trigger the Celery task
        task = long_running_task.delay()
        return JsonResponse({'task_id': task.id, 'status': 'Task started!'})

    return render(request, 'start_task.html')

from .models import RetrievedAccount

def create_retrieved_account(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        RetrievedAccount.objects.create(phone_number=phone_number)
        return redirect('retrieved_account_list')  # هدایت به لیست حساب‌های ذخیره شده
    return render(request, 'create_retrieved_account.html')

def retrieved_account_list(request):
    accounts = RetrievedAccount.objects.all()  # دریافت تمام حساب‌های بازیابی‌شده
    return render(request, 'retrieved_account_list.html', {'accounts': accounts})


def update_username(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')

        try:
            # پیدا کردن حساب بر اساس شماره تلفن
            account = RetrievedAccount.objects.get(phone_number=phone_number)
            # به‌روزرسانی نام کاربری
            account.username = username
            account.save()  # ذخیره تغییرات

            return redirect('retrieved_account_list')  # هدایت به لیست حساب‌ها پس از به‌روزرسانی
        except RetrievedAccount.DoesNotExist:
            return render(request, 'update_username.html', {'error': 'شماره تلفن یافت نشد.'})

    return render(request, 'update_username.html')

