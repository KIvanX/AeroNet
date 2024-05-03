import json
import os
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from AeroNet.settings import EMAIL_ADDRESS, EMAIL_PASSWORD
from django.contrib.auth.hashers import make_password
from authorization.serializers import *
from AeroNet import settings
from Flights.models import Booking, Ticket
import stripe


class StaffAPIViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + f'success/?ticket_id={request.GET.get("ticket_id")}&'
                                         f'user_id={request.GET.get("user_id")}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': 'price_1N02BKJoNCkb39bTZtEL0Ia3',
                        'quantity': 1,
                    }
                ]
            )
            return redirect(checkout_session['url'])
        except Exception as e:
            return JsonResponse({'error': str(e)})


class SuccessView(View):
    def get(self, request):
        ticket = Ticket.objects.get(id=request.GET.get('ticket_id', 0))
        user = User.objects.get(id=request.GET.get('user_id', 0))
        Booking(price=10000, ticket=ticket, user=user).save()
        return redirect(f'http://localhost:8080/')


class CancelledView(View):
    def get(self, request):
        return redirect(f'http://localhost:8080/')


def send_email(email, subject, text):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email

    msgText = MIMEText(f'<h3>{text}</h3>', 'html')
    msg.attach(msgText)

    smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)
    smtpObj.starttls()
    smtpObj.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtpObj.sendmail(msg['From'], msg['To'], msg.as_string().encode())


class recovering_password(viewsets.ViewSet):
    @staticmethod
    def get_code(request: WSGIRequest):
        code = str(random.randint(10 ** 5, 10 ** 6))
        send_email(request.GET.get('email'),
                   'Сброс пароля на сайте AeroNet',
                   f'Код для восстановления пароля на сайте AeroNet: {code}')
        return JsonResponse({'result': code})

    @staticmethod
    def set_new(request: WSGIRequest):
        data = json.loads(request.body)['headers']
        user = User.objects.get(email=data['email'])

        user.password = make_password(data['password'])
        user.save()

        return JsonResponse({'result': 'OK'})


class set_email(viewsets.ViewSet):
    def edit(self, request: WSGIRequest):
        data = json.loads(request.body)
        if request.user.check_password(data['current_password']):
            request.user.email = data['new_email']
            request.user.save()
            return JsonResponse({'result': 'OK'})
        else:
            return JsonResponse({'result': 'ERROR'})


class GetMyImage(viewsets.ViewSet):
    def get_image(self, request: WSGIRequest):
        with open(os.path.join(settings.BASE_DIR, 'static/default.png'), 'rb') as f:
            return HttpResponse(f.read(), content_type='content/image')

    def update(self, request: WSGIRequest):
        print(request.POST)
        return JsonResponse({'result': 'OK'})
