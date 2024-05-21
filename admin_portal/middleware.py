from django.shortcuts import redirect
from django.urls import resolve


class AdminAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if user is authenticated and has admin permissions
        if request.path.startswith('/admin/') \
                and not request.user.is_authenticated \
                and resolve(request.path_info).route != 'admin/login/':
            return redirect('/admin/login')

        return response
