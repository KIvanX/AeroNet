from django.test import TestCase
from AeroNet.wsgi import *
from Flights.models import Flight, Airport
from Flights.views import get_flights_to_set


class FlightsTestCases(TestCase):
    def setUp(self):
        self.airport_a = Airport(name='airport_a', city='airport_a', coordinates='(0, 0)')
        self.airport_b = Airport(name='airport_b', city='airport_b', coordinates='(1, 1)')
        self.airport_c = Airport(name='airport_c', city='airport_c', coordinates='(2, 2)')

        self.f1 = Flight(departure_airport=self.airport_a, arrival_airport=self.airport_b)
        self.f2 = Flight(departure_airport=self.airport_b, arrival_airport=self.airport_c)
        self.f3 = Flight(departure_airport=self.airport_c, arrival_airport=self.airport_a)

    def test_set_flights(self):
        res1 = get_flights_to_set([self.f1, self.f3, self.f1, self.f2, self.f3], limit=10)
        self.assertEquals(len(res1), 3)

        res2 = get_flights_to_set([self.f1, self.f2, self.f3], limit=2)
        self.assertEquals(len(res2), 2)

