from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from app.models import Job, Apply
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_jobs(request):
    user = request.user
    jobs = Job.objects.filter(creator_id=user.id)

    paginator = Paginator(jobs, 10)
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    context = {
        'type': 'is_normal_user',
        'jobs': jobs,
        'pages': range(1, jobs.paginator.num_pages + 1)
    }
    return render(request, 'admin/jobs.html', context)


def get_applies(request):
    user = request.user
    applies = Apply.objects.filter(hr_process=user.id)

    paginator = Paginator(applies, 10)
    page = request.GET.get('page')
    try:
        applies = paginator.page(page)
    except PageNotAnInteger:
        applies = paginator.page(1)
    except EmptyPage:
        applies = paginator.page(paginator.num_pages)

    context = {
        'type': 'is_normal_user',
        'applies': applies,
        'pages': range(1, applies.paginator.num_pages + 1)
    }
    return render(request, 'admin/applies.html', context)