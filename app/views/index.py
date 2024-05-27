from django.shortcuts import render
from ..models.company import Company
from ..models.job import Job

def index(request):
    companies = Company.objects.all()
    jobs = Job.objects.filter(status=1).order_by('-created_at')[:15]
    hot_jobs = Job.objects.filter(status=1).order_by('-count_apply')[:15]
    context = {
        'companies': companies,
        'jobs': jobs,
        'hot_jobs': hot_jobs
    }
    return render(request, 'app/index.html', context)

def search(request):
    query = request.GET.get('param')
    jobs = Job.objects.all()
    hot_jobs = Job.objects.filter(status=1).order_by('-count_apply')[:15]
    if query:
        jobs = jobs.filter(title__icontains=query)
    
    context = {
        'jobs': jobs,
        'hot_jobs': hot_jobs,
        'param': query
    }
    return render(request, 'app/filter.html', context)