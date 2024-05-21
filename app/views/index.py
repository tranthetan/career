from django.shortcuts import render
from ..models.company import Company
from ..models.job import Job

def index(request):
    companies = Company.objects.all()
    jobs = Job.objects.all()
    context = {
        'companies': companies,
        'jobs': jobs
    }
    return render(request, 'index.html', context)

def search(request):
    query = request.GET.get('param')
    jobs = Job.objects.all()
    
    if query:
        jobs = jobs.filter(title__icontains=query)
    
    context = {
        'jobs': jobs,
        'param': query
    }
    return render(request, 'filter.html', context)