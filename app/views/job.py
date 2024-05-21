from django.shortcuts import render
from ..models.job import Job

def show(request, job_id):
    job = Job.objects.get(id = job_id)
    company = job.company
    context = {
        'job': job,
        'company': company
    }
    return render(request, 'detail.html', context)