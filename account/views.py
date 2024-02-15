from django.shortcuts import redirect, render, reverse

from .forms import LoginForm, RegisterForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration passed.")
        else:
            messages.error(request, "Registration failed.")
    return render(request, "account/registration.html", {"register_form": RegisterForm})


def logging_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('welcome'))
            else:
                messages.error(request, "Invalid login credentials.")
    return render(request, "account/login.html", {"login_form": LoginForm})


def logging_out(request):
    logout(request)
    return redirect(reverse('welcome'))
