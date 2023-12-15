from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.details, name="details"),
    path('doctors', views.doctors_list, name="doctors"),
    path('reservation', views.reservation, name="reservation")
]
