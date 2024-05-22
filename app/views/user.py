from django.shortcuts import render, redirect
from ..forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth import login

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