from django.shortcuts import render

from django.http import HttpResponse

from visits.models import Visit


def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "Check the available visits on our page.",
                   "visits_all": Visit.objects.all(),
                   "visits_available": Visit.objects.filter(available=True),
                   "visits_num": Visit.objects.filter(available=True).count()})


def about(request):
    return HttpResponse("This is a website of our Clinic. You can book the services which we provide.")
