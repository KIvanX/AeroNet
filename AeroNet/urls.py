
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authorization.views import *
from Flights.views import *
from .yasg import doc_urls

router = routers.DefaultRouter()
router.register(r'staff', StaffAPIViewSet)
router.register(r'airports', AirportAPIViewSet)
router.register(r'aircraft', AircraftAPIViewSet)
router.register(r'seats', SeatAPIViewSet)
router.register(r'flights', FlightAPIViewSet)
router.register(r'tickets', TicketAPIViewSet)
router.register(r'bookings', BookingAPIViewSet)


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('auth/user/recovering_password/', recovering_password.as_view({'get': 'get_code', 'post': 'set_new'})),
    path('auth/user/set_email/', set_email.as_view({'post': 'edit'})),
    path('auth/user/image/', GetMyImage.as_view({'get': 'get_image', 'post': 'update'})),

    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/get_flights/', flight_by_filters),

    path('payment/', create_checkout_session),
    path('success/', SuccessView.as_view()),
    path('cancelled/', CancelledView.as_view()),

    path('delete_booking/<int:pk>', DeleteBookingView.as_view()),
] + doc_urls
