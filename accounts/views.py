from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout


class LoginView(generic.View):

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, request.POST)
        print(request.POST)
        print(form.data)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
        return redirect(reverse_lazy('main_page'))


class RegisterView(generic.View):

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = UserCreationForm(request.POST)
        print(form.data)
        if form.is_valid():
            print('Form valid')
            form.save()
        else:
            print('Form not valid')

        return redirect(reverse_lazy('main_page'))


@login_required(redirect_field_name='main_page')
def logout_user(request):
    if request.method == 'GET':
        logout(request)
        return redirect('main_page')
    if request.method == 'POST':
        return redirect('main_page')
