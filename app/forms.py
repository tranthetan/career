from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_normal_user = True
        user.is_superadmin = False
        user.is_staff = False
        if commit:
            user.save()
        return user