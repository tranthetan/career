from django.shortcuts import render
from ..models import Job, Apply

def show(request, job_id):
    job = Job.objects.get(id = job_id)
    company = job.company
    context = {
        'job': job,
        'company': company
    }
    return render(request, 'app/detail.html', context)

def apply(request, job_id):
    if request.method == "POST":
        user = request.user
        job = Job.objects.get(id = job_id)
        if job:
            cover_letter = request.POST.get('cover_letter')
            resume = request.FILES.get('resume')
            resume_path = default_storage.save(f'resume/{resume.name}', resume)
            Apply.objects.create(
                hr_proces = job.creator_id,
                cover_letter = cover_letter,
                resume_path = default_storage.url(resume_path),
                status = 0,
                user_id = user.id,
                company_id = job.company_id,
                job_id = job_id
            )
            messages.success(request, 'Apply successfully!')
        else:
            messages.success(request, 'Apply failed!')
    return redirect(reverse('job-detail', args=[job_id]))
