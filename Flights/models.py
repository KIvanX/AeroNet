from django.db import models
from django.contrib.auth.models import User


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    coordinates = models.CharField(max_length=40)

    def __str__(self):
        return self.name + ' ' + self.city


class Aircraft(models.Model):
    model = models.CharField(max_length=30)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.model


class Seat(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=20)

    def __str__(self):
        return self.seat_number + '(' + str(self.aircraft) + ')'


class Flight(models.Model):
    departure_airport = models.ForeignKey(Airport, null=True, on_delete=models.SET_NULL, related_name='airport_from')
    arrival_airport = models.ForeignKey(Airport, null=True, on_delete=models.SET_NULL, related_name='airport_to')
    departure_date = models.DateTimeField(null=True)
    arrival_date = models.DateTimeField(null=True)
    aircraft = models.ForeignKey(Aircraft, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.departure_airport.city) + '-' + str(self.arrival_airport.city)


class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.flight) + '(' + str(self.seat) + ')'


class Booking(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)

    def __str__(self):
        return str(self.ticket) + '(' + str(self.user) + ')'
