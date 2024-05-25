from django import forms
from .models import User, Company, HrRegister
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_nomal_user = True
        user.is_superuser = False
        user.is_staff = False
        if commit:
            user.save()
        return user