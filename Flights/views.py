
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from AeroNet.settings import REST_FRAMEWORK
from Flights.serializers import *


def flight_by_filters(request):
    dep = Airport.objects.filter(city__icontains=request.GET.get('from', ''))
    arr = Airport.objects.filter(city__icontains=request.GET.get('to', ''))
    flights = Flight.objects.filter(arrival_airport__in=arr) & Flight.objects.filter(departure_airport__in=dep)
    return JsonResponse({'results': FlightSerializer(flights, many=True).data})


class AirportAPIViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [permissions.IsAuthenticated]


class AircraftAPIViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SeatAPIViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    # permission_classes = [permissions.IsAuthenticated]


class FlightAPIViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    @action(detail=False, methods=['GET'], name='Get by')
    def by(self, request, *args, **kwargs):
        dep = Airport.objects.filter(city__icontains=request.GET.get('from', ''))
        arr = Airport.objects.filter(city__icontains=request.GET.get('to', ''))
        flights = Flight.objects.filter(arrival_airport__in=arr) & Flight.objects.filter(departure_airport__in=dep)
        if 'set' in request.GET:
            flights = get_flights_to_set(flights, REST_FRAMEWORK['PAGE_SIZE'] * int(request.GET.get('page', '1')))
        paginator = Paginator(flights, REST_FRAMEWORK['PAGE_SIZE'])
        flights_page = FlightSerializer(paginator.get_page(request.GET.get('page')), many=True).data

        return Response(flights_page)


def get_flights_to_set(flights, limit):
    set_flights = set()
    new_flights = []
    for fl in flights:
        if str(fl) not in set_flights:
            new_flights.append(fl)
            set_flights.add(str(fl))
            if len(set_flights) >= limit:
                return new_flights
    return new_flights


class TicketAPIViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @action(detail=False, methods=['GET'], name='Get by')
    def by(self, request, *args, **kwargs):
        busy_tickets = Booking.objects.all().values('ticket_id')
        tickets = Ticket.objects.filter(flight_id=request.GET.get('flight_id', '')).filter(~Q(id__in=busy_tickets))
        return Response(TicketSerializer(tickets, many=True).data)


class DeleteTicketView(View):
    def post(self, request, pk):
        Ticket.objects.get(pk=pk).delete()
        return JsonResponse({'results': 'true'})


class BookingAPIViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET'], name='Get by')
    def by(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(user_id=request.GET.get('user_id', ''))
        return Response(BookingSerializer(bookings, many=True).data)
