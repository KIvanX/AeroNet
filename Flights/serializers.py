
from rest_framework.serializers import ModelSerializer
from Flights.models import *
from authorization.serializers import User


class AirportSerializer(ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class AircraftSerializer(ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'


class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class FlightSerializer(ModelSerializer):
    departure_airport = AirportSerializer()
    arrival_airport = AirportSerializer()
    aircraft = AircraftSerializer()

    class Meta:
        model = Flight
        fields = '__all__'


class TicketSerializer(ModelSerializer):
    seat = SeatSerializer()
    flight = FlightSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'


class BookingSerializer(ModelSerializer):
    ticket = TicketSerializer()

    class Meta:
        model = Booking
        fields = '__all__'
