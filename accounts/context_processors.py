from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms as auth_forms


def login_form(request):
    return {
        'login_form': auth_forms.AuthenticationForm,
        'register_form': UserCreationForm(),
        'password_reset_form': auth_forms.PasswordResetForm,
    }

