from django.shortcuts import redirect, render, reverse

from django.http import HttpResponse

from .forms import LoginForm, RegisterForm

from django.contrib.auth import authenticate, login, logout

from visits.models import Visit


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "account/successful_reg.html")
        else:
            return render(request, "account/unsuccessful_reg.html")
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
                return HttpResponse('disabled account')
    # return render_to_response('login.html', form, RequestContext)
    return render(request, "account/login.html", {"login_form": LoginForm})


def logging_out(request):
    logout(request)
    return redirect(reverse('welcome'))


def history(request):
    context = {}
    if request.user.is_active:
        context["visits_patient_history"] = Visit.objects.filter(past=True, patient=request.user)

    return render(request, "account/visit_history.html", context)


def settings(request):
    return render(request, "account/settings.html")
