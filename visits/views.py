from django.shortcuts import get_object_or_404, redirect, render, reverse, HttpResponse

from visits.models import Visit, Doctor

from website.views import out_of_date

from visits.forms import VisitSearchForm


def details(request, id):
    visit = get_object_or_404(Visit, pk=id)
    context = {
        "visit": visit,
        "visits_patient_upcoming": Visit.objects.filter(past=False, patient=request.user),
        "visits_available": Visit.objects.filter(past=False, patient=None)
    }
    return render(request, "visits/details.html", context)


def doctors_list(request):
    return render(request, "visits/doctors_list.html",
                  {"doctors": Doctor.objects.all()})


def reservation(request, id):
    visit = get_object_or_404(Visit, pk=id)
    out_of_date(visit)
    if visit.patient is None:
        visit.patient = request.user
        visit.save()
        return redirect(reverse('welcome'))
    else:
        return render(request, "visits/unavailable_visit.html")


def calendar(request):
    for visit in Visit.objects.filter(past=False):
        out_of_date(visit)

    context = {'form': VisitSearchForm}

    qs = Visit.objects.filter(past=False, patient=None)
    spec_query = request.GET.get('specialization')
    doc_query = request.GET.get('doctor')
    loc_query = request.GET.get('location')

    if spec_query != "" and spec_query is not None:
        qs = qs.filter(doctor__specialization=spec_query)
    if doc_query != "" and doc_query is not None:
        qs = qs.filter(doctor=doc_query)
    if loc_query != "" and loc_query is not None:
        qs = qs.filter(location=loc_query)

    context['queryset'] = qs

    return render(request, "visits/calendar.html", context)


def cancel_visit(request, id):
    visit = get_object_or_404(Visit, pk=id)
    visit.patient = None
    visit.save()
    return redirect(reverse('welcome'))
