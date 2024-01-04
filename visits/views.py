from django.shortcuts import get_object_or_404, redirect, render, reverse, HttpResponse

from visits.models import Visit, Doctor


def details(request, id):
    visit = get_object_or_404(Visit, pk=id)
    return render(request, "visits/details.html", {"visit": visit})


def doctors_list(request):
    return render(request, "visits/doctors_list.html",
                  {"doctors": Doctor.objects.all()})


def reservation(request, id):
    visit = get_object_or_404(Visit, pk=id)
    visit.available = False
    visit.save()
    return redirect(reverse('welcome'))
