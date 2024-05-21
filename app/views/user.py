from django.shortcuts import render
from ..forms import RegisterUserForm

def register(request):
    return render(request, 'app/register.html')

def action_register(request):
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