from django.contrib import admin
from Flights.models import *

# Register your models here.
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Seat)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Booking)