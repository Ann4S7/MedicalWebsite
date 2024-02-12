from django.urls import path

from . import views

urlpatterns = [
    path('visits/<int:id>', views.details, name="details"),
    path('doctors', views.doctors_list, name="doctors"),
    path('visits/<int:id>/reservation', views.reservation, name="reservation"),
    path('visits', views.calendar, name="calendar"),
    path('schedule/<int:id>', views.schedule_details, name="schedule_details"),
    path('schedule/<int:id>/cancel', views.cancel_visit, name="cancel")
]
