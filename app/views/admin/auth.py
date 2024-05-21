from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.http import HttpResponseRedirect
from app.models import User


def index(request):
    return render(request, 'admin/index.html')


def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect(reverse('admin-index'))

        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)

            user_obj = authenticate(username=username, password=password)
            if user_obj:
                if user_obj.is_superuser or user_obj.is_staff:
                    login(request, user_obj)
                    return redirect(reverse('admin-index'))
                else:
                    messages.info(request, 'Không có quyền rồi người anh em à')
                    return redirect(reverse('admin-login'))
            else:
                messages.info(request, 'Invalid username or password')
                return redirect(reverse('admin-login'))

        return render(request, 'admin/login.html', {})
    except Exception as e:
        print(e)


def admin_logout(request):
    logout(request)
    return redirect(reverse('admin-logout'))

