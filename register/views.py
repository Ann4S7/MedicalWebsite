from django.shortcuts import render, redirect

from register.forms import RegisterForm


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "register/successful_reg.html")
        else:
            return render(request, "register/unsuccessful_reg.html")
    return render(request, "register/registration.html", {"register_form": RegisterForm})
