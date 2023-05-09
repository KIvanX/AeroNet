import datetime
import random
import requests
from AeroNet.wsgi import *
import psycopg2
from Flights.models import *
from authorization.models import *


class Database:
    def __init__(self):
        self.con = psycopg2.connect(
            dbname="demo",
            user="postgres",
            password="pass",
            host="localhost",
            port=5432
        )
        self.cur = self.con.cursor()

    def fill_aircraft(self):
        self.cur.execute('SELECT * FROM aircrafts_data')
        for e in self.cur.fetchall():
            Aircraft(model=e[1]['en'], age=random.randint(0, 10)).save()

    def fill_airports(self):
        self.cur.execute('SELECT * FROM airports_data')
        for e in self.cur.fetchall():
            Airport(name=e[1]['ru'], city=e[2]['ru'], coordinates=e[3]).save()

    def fill_flights(self):
        code_to_airport = {}
        self.cur.execute('SELECT * FROM airports_data')
        for e in self.cur.fetchall():
            code_to_airport[e[0]] = Airport.objects.get(name=e[1]['ru'])

        code_to_aircraft = {}
        self.cur.execute('SELECT * FROM aircrafts_data')
        for e in self.cur.fetchall():
            code_to_aircraft[e[0]] = Aircraft.objects.get(model=e[1]['en'])

        self.cur.execute('SELECT * FROM flights')
        for e in self.cur.fetchall():
            Flight(departure_airport=code_to_airport[e[4]],
                   arrival_airport=code_to_airport[e[5]],
                   aircraft=code_to_aircraft[e[7]],
                   departure_date=e[2],
                   arrival_date=e[3]).save()

    def fill_users(self):
        users = requests.get('https://api.randomdatatools.ru', params={'count': 100, 'typeName': 'rare'}).json()
        for user in users:
            User(first_name=user['FirstName'], second_name=user['LastName'],
                 password=user['Password'], email=user['Email']).save()

    def fill_staff(self):
        prof = ['Пилот гражданской авиации', 'Командир воздушного судна', 'Бортпроводник', 'Бортинженер',
                'Авиадиспетчер', 'Агент по регистрации', 'Агент по сопровождению', 'Менеджер авиакомпаний',
                'Сециалист по паспортному контролю', 'Специалист по авиабезопасности', 'Техник и наладчик',
                'Инженер по сигнальному оборудованию', 'Диспетчер по техническому обслуживанию',
                'IT-специалист', 'Таможенник']
        users = User.objects.all()
        for _ in range(random.randint(100, 300)):
            Staff(user_id=random.choice(users).id, profession=random.choice(prof), is_admin=random.choice([1, 0])).save()

    def fill_seats(self):
        for aircraft in Aircraft.objects.all():
            for i in range(random.randint(5, 50)):
                Seat(aircraft=aircraft, seat_number=str(i // 6 + 1) + chr(ord('A') + i % 6)).save()

    def fill_tickets(self):
        seats = {}
        for ai in Aircraft.objects.all():
            seats[ai.id] = list(Seat.objects.filter(aircraft=ai))

        for fl in Flight.objects.all():
            random.shuffle(seats[fl.aircraft.id])
            free_seats = seats[fl.aircraft.id][:random.randint(0, 10)]
            for seat in free_seats:
                Ticket(seat=seat, flight=fl).save()

    def fill_bookings(self):
        tickets = Ticket.objects.all()
        for user in User.objects.all():
            for _ in range(random.randint(0, 3)):
                Booking(user=user, ticket=random.choice(tickets), price=random.randint(10, 100) * 500).save()


db = Database()

