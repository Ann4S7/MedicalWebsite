from django.shortcuts import redirect, render, reverse

from django.http import HttpResponse

from .forms import LoginForm

from django.contrib.auth import authenticate, login, logout


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
                return HttpResponse('disabled account')
    # return render_to_response('login.html', form, RequestContext)
    return render(request, "account/login.html", {"login_form": LoginForm})


def logging_out(request):
    logout(request)
    return redirect(reverse('welcome'))
