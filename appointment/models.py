from django.db import models
from django.utils import timezone

from hospital.models import Doctor

NULLABLE = {
    'null': True,
    'blank': True
}

NOT_NULLABLE = {
    'null': False,
    'blank': False
}

"""Создаем приложение для записи на прием к Врачу"""

class Appointment(models.Model):
    choices_time = (
        ('morning', 'Morning'),
        ('evening', 'Evening')
    )
    name = models.CharField(max_length=120, verbose_name='Имя')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    doctors = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врачи')
    date = models.DateField(default=timezone.now)
    time = models.CharField(choices=choices_time, max_length=10)
    extra_note = models.TextField(**NULLABLE, verbose_name='Дополнительное примечание')

    class Meta:
        verbose_name = 'Встреча'
        verbose_name_plural = "Встречи"

    def __str__(self):
        return f'{self.name} - {self.doctors.name}'
