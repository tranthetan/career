from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from app.models import Job, Apply, Company, Career, WorkType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from django.db import models
from django.contrib import messages


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
            messages.success(request, 'Cập nhật thành công.')

        job = Job.objects.filter(id=job_id).first()
        companies = Company.objects.all()
        careers = Career.objects.all()
        work_types = WorkType.objects.all()
        context = {'job': job, 'companies': companies, 'careers': careers, 'work_types': work_types}

        return render(request, 'admin/job-edit.html', context)
    except Exception as e:
        print(e)


def insert_job(request):
    try:
        if request.method == 'POST':
            new_job = Job(
                title=request.POST.get('title', ''),
                description=request.POST.get('description', ''),
                salary_range=request.POST.get('salary_range', ''),
                level=request.POST.get('level'),
                status=1 if request.POST.get('status') == 'on' else 0,
                career_id=request.POST.get('career'),
                company_id=request.POST.get('company'),
                work_type_id=request.POST.get('work_type'),
                creator_id=request.user.id,
                count_apply=0
            )
            new_job.save()
            messages.success(request, 'Thêm mới thành công.')

        companies = Company.objects.all()
        careers = Career.objects.all()
        work_types = WorkType.objects.all()
        context = {'companies': companies, 'careers': careers, 'work_types': work_types}

        return render(request, 'admin/job-insert.html', context)
    except Exception as e:
        print(e)


def delete_job(request, job_id):
    try:
        if request.method == 'POST':
            job = get_object_or_404(Job, pk=job_id)
            job.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False})

def view_resume(request, apply_id):
    try:
        apply = Apply.objects.get(id=apply_id)
        apply.status = 1
        apply.save()
        
        response_data = {
            'success': True,
            'message': 'Status updated successfully',
            'resume_path': apply.resume_path,
        }
    except Apply.DoesNotExist:
        response_data = {
            'success': False,
            'message': 'Apply object not found',
        }
    except Exception as e:
        response_data = {
            'success': False,
            'message': str(e),
        }
    
    return JsonResponse(response_data)