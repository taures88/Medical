from django.contrib import admin

from hospital.models import Doctor

"""регистрация в админке"""
admin.site.register(Doctor)
