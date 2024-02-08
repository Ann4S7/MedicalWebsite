from django.contrib.auth.models import User

from django.shortcuts import render

from visits.models import Visit

from datetime import datetime


def welcome(request):
    for visit in Visit.objects.all():
        out_of_date(visit)

    context = {}
    if request.user.is_active:
        context["visits_patient_upcoming"] = Visit.objects.filter(past=False, patient=request.user)

    return render(request, "website/welcome.html", context)


def out_of_date(visit):
    visit_datetime = datetime.combine(visit.date, visit.start_time)
    if visit_datetime < datetime.now():
        visit.past = True
        visit.save()
