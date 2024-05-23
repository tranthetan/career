from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from app.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def users_hr(request):
    users = User.objects.filter(is_staff=1)

    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'type': 'is_staff',
        'users': users,
        'pages': range(1, users.paginator.num_pages + 1)
    }
    return render(request, 'admin/users.html', context)


def users_normal(request):
    users = User.objects.filter(is_nomal_user=1)

    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'type': 'is_normal_user',
        'users': users,
        'pages': range(1, users.paginator.num_pages + 1)
    }
    return render(request, 'admin/users.html', context)


def toggle_user_active(request, user_id):
    try:
        user = get_object_or_404(User, pk=user_id)
        user.is_active = not user.is_active  # Toggle the active status
        user.save()
        return JsonResponse({'success': True})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False})
