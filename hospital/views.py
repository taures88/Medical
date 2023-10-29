from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from hospital.models import Doctor


class hospitalView(TemplateView):
    template_name = 'index.html'


class DoctorListView(ListView):
    queryset = Doctor.objects.all()
    template_name = 'doctor-team.html'


class ListServicesView(TemplateView):
    template_name = 'list_services.html'


class ContactView(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email_from = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = 'Healthcae Contact'

        if name and message and email_from:
            send_mail(
                subject + " - " + name,
                message +
                email_from,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email_from]
            )
            messages.success(request, f'Ваше сообщение отправлено. Спасибо {name}!')

        return redirect('contact')
