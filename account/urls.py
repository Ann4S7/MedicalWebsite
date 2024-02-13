from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.logging_in, name='login'),
    path('logout/', views.logging_out, name='logout')
]
