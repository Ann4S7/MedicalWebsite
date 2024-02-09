from django import forms

from visits.models import Doctor, Location, Specialization


class VisitSearchForm(forms.Form):
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(), required=False, empty_label="")
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=False, empty_label="")
    location = forms.ModelChoiceField(queryset=Location.objects.all(), required=False, empty_label="")
