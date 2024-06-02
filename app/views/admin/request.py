from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from app.models import HrRegister, HRCompany, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def requests(request):
    requests = HrRegister.objects.all()

    paginator = Paginator(requests, 10)
    page = request.GET.get('page')
    try:
        requests = paginator.page(page)
    except PageNotAnInteger:
        requests = paginator.page(1)
    except EmptyPage:
        requests = paginator.page(paginator.num_pages)

    context = {
        'type': 'is_normal_user',
        'requests': requests,
        'pages': range(1, requests.paginator.num_pages + 1)
    }
    return render(request, 'admin/requests.html', context)

def action_approve_or_reject(request, request_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        try:
            hr_request = HrRegister.objects.get(id=request_id)

            if action == '1':
                HRCompany.objects.create(
                    company_id = hr_request.company_id,
                    hr_id = hr_request.user_id
                )
                user = User.objects.get(pk=hr_request.user_id)
                user.is_staff = 1
                user.is_nomal_user = 0
                user.save()
                hr_request.delete()
            else:
                hr_request.delete()

            return JsonResponse({'success': True, 'message': 'Request status updated successfully.'})
        except HrRegister.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Request not found.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})
