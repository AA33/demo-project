from django.contrib import admin
from travel_log.models import Trip, Destination


# Register all models
admin.site.register(Trip)
admin.site.register(Destination)
