from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from app.models import Job, Apply, Company, Career, WorkType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms


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


def edit_job(request, job_id):
    try:
        context = {}
        if request.method == 'POST':
            job = Job.objects.get(pk=job_id)
            job.title = request.POST.get('title')
            job.description = request.POST.get('description')
            job.salary_range = request.POST.get('salary_range')
            job.level = request.POST.get('level')
            job.status = 1 if request.POST.get('status') == 'on' else 0
            job.career_id = request.POST.get('career')
            job.company_id = request.POST.get('company')
            job.work_type_id = request.POST.get('work_type')
            job.save()
            context['status'] = 'success'
            context['message'] = 'Cập nhật thành công.'

        job = Job.objects.filter(id=job_id).first()
        companies = Company.objects.all()
        careers = Career.objects.all()
        work_types = WorkType.objects.all()
        context['job'] = job
        context['companies'] = companies
        context['careers'] = careers
        context['work_types'] = work_types

        return render(request, 'admin/job-edit.html', context)
    except Exception as e:
        print(e)

