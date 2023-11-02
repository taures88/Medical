from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from hospital.models import Doctor

"""основная страница"""


class hospitalView(ListView):
    model = Doctor
    template_name = 'index.html'


"""выводит список врачей"""


class DoctorListView(ListView):
    model = Doctor
    queryset = Doctor.objects.all()
    template_name = 'doctor-team.html'


"""выводит список специализаций"""


class ListServicesView(ListView):
    model = Doctor
    template_name = 'list_services.html'


"""вывод контактов и заполнение формы заявки с отправкой на почту"""


class ContactView(ListView):
    model = Doctor
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email_from = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and message and email_from:
            send_mail(
                subject='Medical+',
                message=f'Уважаемый {name}, Ваша заявка по теме {subject} принята {datetime.now().replace(microsecond=0)}, наш специалист '
                        f'свяжется в ближайшее время.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email_from]
            )
            messages.success(request, f'Ваше сообщение отправлено. Спасибо {name}!')

        return redirect('contact')
