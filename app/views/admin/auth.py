from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.http import HttpResponseRedirect
from app.models import User, Company, Apply
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    user = request.user
    applies_count = Apply.objects.filter(creator_id=user.id, status=1).count()
    context = {
        'applies_count': 100 
    }
    return render(request, 'admin/index.html', context)

def users(request):
    return render(request, 'admin/users.html')

def company(request):
    companies = Company.objects.all()
    
    paginator = Paginator(companies, 10)  # Chia dữ liệu thành các trang, mỗi trang có 10 phần tử
    
    page = request.GET.get('page')
    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        companies = paginator.page(1)
    except EmptyPage:
        companies = paginator.page(paginator.num_pages)
    
    context = {
        'companies': companies,
    }
    return render(request, 'admin/company.html', context)

def admin_login(request):
    try:
        if request.user.is_authenticated and not request.user.is_nomal_user:
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

