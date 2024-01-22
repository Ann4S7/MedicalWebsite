from django.urls import path

from . import views

urlpatterns = [
    path('available/<int:id>', views.details, name="details"),
    path('doctors', views.doctors_list, name="doctors"),
    path('available/<int:id>/reservation', views.reservation, name="reservation"),
    path('available', views.calendar, name="calendar"),
    path('schedule/<int:id>', views.schedule_details, name="schedule_details"),
    path('schedule/<int:id>/cancel', views.cancel_visit, name="cancel")
]
