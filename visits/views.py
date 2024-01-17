from django.shortcuts import get_object_or_404, redirect, render, reverse, HttpResponse

from visits.models import Visit, Doctor

from datetime import datetime


def details(request, id):
    visit = get_object_or_404(Visit, pk=id)
    return render(request, "visits/details.html", {"visit": visit})


def doctors_list(request):
    return render(request, "visits/doctors_list.html",
                  {"doctors": Doctor.objects.all()})


def out_of_date(visit):
    visit_datetime = datetime.combine(visit.date, visit.start_time)
    if visit_datetime < datetime.now():
        visit.available = False
        visit.save()


def reservation(request, id):
    visit = get_object_or_404(Visit, pk=id)
    out_of_date(visit)
    if visit.available is True:
        visit.available = False
        visit.save()
        return redirect(reverse('welcome'))
    else:
        return render(request, "visits/unavailable_visit.html")


def calendar(request):
    return render(request, "visits/calendar.html",
                  {"visits_available": Visit.objects.filter(available=True),
                   "visits_available_num": Visit.objects.filter(available=True).count()})


def schedule_details(request, id):
    visit = get_object_or_404(Visit, pk=id)
    return render(request, "visits/schedule_details.html", {"visit": visit})


def cancel_visit(request, id):
    visit = get_object_or_404(Visit, pk=id)
    visit.available = True
    visit.patient = None
    visit.save()
    return redirect(reverse('welcome'))
