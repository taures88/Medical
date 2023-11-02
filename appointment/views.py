from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from hospital.models import Doctor
from .models import Appointment


"""Вывод страницы с записью и отправка письма"""

class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'object_list': Doctor.objects.all()
        }
        return render(request, 'appointment/appointments.html', context)

    def post(self, request, *args, **kwargs):

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        extra_note = request.POST.get('message')
        doctor_id = request.POST.get('doctor')

        if doctor_id:
            doctor = get_object_or_404(Doctor, id=doctor_id)

        if name and phone and email and doctor and date and time and extra_note:
            Appointment.objects.create(name=name, phone=phone, email=email, doctors=doctor, extra_note=extra_note,
                                       time=time, date=date)
            send_mail(
                subject='Medical+',
                message=f'Уважаемый {name}, Вы записаны к врачу {doctor} {date}, для подтверждения более точного времени '
                        f'с Вами свяжется наш специалист.\nПрекрасного дня!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )
            messages.success(request, 'Запись прошла успешно!')
        return redirect('appointment')
