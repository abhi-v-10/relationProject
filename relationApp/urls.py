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

    path('view-doctors-patients/', views.view_doctors_patients, name='view_doctors_patients'),
    path('view-courses-students/', views.view_courses_students, name='view_courses_students'),
    path('view-employees-idcards/', views.view_employees_idcards, name='view_employees_idcards'),

    path('api_doctors/', views.api_doctors, name='api_doctors'),
    path('api_patients/', views.api_patients, name='api_patients'),
    path('api_courses/', views.api_courses, name='api_courses'),
    path('api_students/', views.api_students, name='api_students'),
    path('api_employees/', views.api_employees, name='api_employees'),
    path('api_idcards/', views.api_idcards, name='api_idcards'),

    path('api_doctors-patients/', views.api_doctors_with_patients, name='api_doctors_patients'),
    path('api_courses-students/', views.api_courses_with_students, name='api_courses_students'),
    path('api_employees-idcards/', views.api_employees_with_idcards, name='api_employees_idcards'),

]
