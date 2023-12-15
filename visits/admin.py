from django.contrib import admin

from .models import Visit, Location, Specialization, Doctor

admin.site.register(Visit)
admin.site.register(Location)
admin.site.register(Specialization)
admin.site.register(Doctor)
