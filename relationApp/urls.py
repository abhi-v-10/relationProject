from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-doctor/', views.create_doctor, name='create_doctor'),
    path('create-course/', views.create_course, name='create_course'),
    path('create-employee/', views.create_employee, name='create_employee'),

    path('create-patient/', views.create_patient, name='create_patient'),
    path('create-student/', views.create_student, name='create_student'),
    path('create-idcard/', views.create_idcard, name='create_idcard'),
]
