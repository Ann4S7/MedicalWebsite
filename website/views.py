from django.shortcuts import render

from django.http import HttpResponse

from visits.models import Visit

from datetime import datetime


def welcome(request):
    for visit in Visit.objects.all():
        out_of_date(visit)
    return render(request, "website/welcome.html",
                  {"message": "Check the available visits on our page.",
                   "visits_all": Visit.objects.all(),
                   "visits_available": Visit.objects.filter(available=True),
                   "visits_num": Visit.objects.filter(available=True).count()})


def about(request):
    return HttpResponse("This is a website of our Clinic. You can book the services which we provide.")


def out_of_date(visit):
    visit_datetime = datetime.combine(visit.date, visit.start_time)
    if visit_datetime < datetime.now():
        visit.available = False
        visit.save()
