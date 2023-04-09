
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authorization.views import *
from Flights.views import *
from .yasg import doc_urls

router = routers.DefaultRouter()
router.register(r'users', UserAPIViewSet)
router.register(r'staff', StaffAPIViewSet)
router.register(r'airports', AirportAPIViewSet)
router.register(r'aircraft', AircraftAPIViewSet)
router.register(r'seats', SeatAPIViewSet)
router.register(r'flights', FlightAPIViewSet)
router.register(r'tickets', TicketAPIViewSet)
router.register(r'bookings', BookingAPIViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + doc_urls
