from django.contrib.auth.models import User

from django.shortcuts import render

from django.http import HttpResponse

from visits.models import Visit

from datetime import datetime


def welcome(request):
    for visit in Visit.objects.all():
        out_of_date(visit)
    if request.user.is_active:
        return render(request, "website/welcome.html",
                      {"visits_available_num": Visit.objects.filter(available=True).count(),
                       "visits_patient": Visit.objects.filter(patient=request.user)})
    else:
        return render(request, "website/welcome.html")


def about(request):
    return HttpResponse("This is a website of our Clinic. You can book the services which we provide.")


def out_of_date(visit):
    visit_datetime = datetime.combine(visit.date, visit.start_time)
    if visit_datetime < datetime.now():
        visit.available = False
        visit.save()
