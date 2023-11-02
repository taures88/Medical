from django.urls import path
from . import views


urlpatterns = [
    path('', views.hospitalView.as_view(), name='hospital'), # основная страница

    path('doctor/', views.DoctorListView.as_view(), name='doctor_team'), # информация о врачах

    path('list/', views.ListServicesView.as_view(), name='list_services'), # список специализаций

    path('contact/', views.ContactView.as_view(), name='contact'), # контактная форма

]