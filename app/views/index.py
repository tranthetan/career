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