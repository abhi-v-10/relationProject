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

]
