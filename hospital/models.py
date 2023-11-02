from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}

NOT_NULLABLE = {
    'null': False,
    'blank': False
}

"""создание модели Врач"""
class Doctor(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя')
    speciality = models.CharField(max_length=120, verbose_name='Специальность')
    picture = models.ImageField(upload_to="doctors/", verbose_name='Изображение')
    experience = models.TextField(verbose_name='Опыт')

    twitter = models.CharField(max_length=120, **NULLABLE)
    facebook = models.CharField(max_length=120, **NULLABLE)
    instagram = models.CharField(max_length=120, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
