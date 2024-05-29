from django.shortcuts import render, redirect, reverse
from ..forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.core.files.storage import default_storage
from django.conf import settings
from ..models import User, Company, HrRegister

def register_form(request):
    return render(request, 'app/register.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "đăng ký thành công.")
            return redirect('home')
        else:
            messages.error(request, "đăng ký Không thành công")
    else:
        form = RegisterUserForm()
    return render(request, 'app/register.html', {'form': form})

def hr_register(request):
    return render(request, 'app/hr_register.html')

def hr_register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        website = request.POST.get('website')
        user_id = request.POST.get('user_id')
        thumbnail = request.FILES.get('thumbnail')

        file_name = default_storage.save(f'companies/{thumbnail.name}', thumbnail)
        company = Company(
            name=name,
            address=address,
            website=website,
            thumbnail=default_storage.url(file_name)
        )
        company.save()

        hr_register = HrRegister(
            company_id=company.id,
            user_id=user_id,
            status=False
        )
        hr_register.save()

        messages.success(request, 'HR and Company have been created successfully!')

    return redirect('home')