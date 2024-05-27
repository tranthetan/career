from django.contrib import admin
from django.urls import path
from .views.admin import auth
from .views.admin import user, job, request

urlpatterns = [
    path('', auth.index, name='admin-index'),
    path('users-hr/', user.users_hr, name='users-hr'),
    path('users-normal/', user.users_normal, name='users-normal'),
    path('toggle-user-active/<int:user_id>/', user.toggle_user_active, name='toggle_user_active'),
    path('login/', auth.admin_login, name='admin-login'),
    path('logout/', auth.admin_logout, name='admin-logout'),
    path('company/', auth.company, name='admin-company'),
    path('jobs/', job.get_jobs, name='admin-jobs'),
    path('jobs/edit/<int:job_id>/', job.edit_job, name='admin-edit-job'),
    path('jobs/insert/', job.insert_job, name='admin-insert-job'),
    path('jobs/delete/<int:job_id>/', job.delete_job, name='admin-delete-job'),
    path('hr/applies', job.get_applies, name='applies'),
    path('requests', request.requests, name='requests'),
    path('request/<int:request_id>/approve-or-reject', request.action_approve_or_reject, name='approve-or-reject'),
]