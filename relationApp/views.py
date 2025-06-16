
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Doctor, Patient, Course, Student, Employee, IDCard

def home(request):
    return render(request, "home.html")


def create_doctor(request):
    error = None
    if request.method == "POST":
        name = request.POST.get("name")
        try:
            Doctor.objects.create(name=name)
            return redirect("create_doctor")
        except IntegrityError:
            error = "Doctor with this name already exists."
    return render(request, "create_doctor.html", {"error": error})

def create_patient(request):
    doctors = Doctor.objects.all()
    error = None
    if request.method == "POST":
        name = request.POST.get("name")
        doctor_id = request.POST.get("doctor")
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            Patient.objects.create(name=name, doctor=doctor)
            return redirect("create_patient")
        except Doctor.DoesNotExist:
            error = "Selected doctor does not exist."
        except IntegrityError:
            error = "Error while creating patient."
    return render(request, "create_patient.html", {"doctors": doctors, "error": error})

def create_course(request):
    error = None
    if request.method == "POST":
        name = request.POST.get("name")
        try:
            Course.objects.create(name=name)
            return redirect("create_course")
        except IntegrityError:
            error = "Course with this name already exists."
    return render(request, "create_course.html", {"error": error})

def create_student(request):
    courses = Course.objects.all()
    error = None
    if request.method == "POST":
        name = request.POST.get("name")
        selected_courses = request.POST.getlist("courses")
        try:
            student = Student.objects.create(name=name)
            student.courses.set(selected_courses)
            return redirect("create_student")
        except IntegrityError:
            error = "Error while creating student."
    return render(request, "create_student.html", {"courses": courses, "error": error})

def create_employee(request):
    error = None
    if request.method == "POST":
        name = request.POST.get("name")
        try:
            Employee.objects.create(name=name)
            return redirect("create_employee")
        except IntegrityError:
            error = "Employee with this name already exists."
    return render(request, "create_employee.html", {"error": error})

def create_idcard(request):
    employees = Employee.objects.all()
    error = None
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        id_number = request.POST.get("id_number")
        try:
            employee = Employee.objects.get(id=employee_id)
            IDCard.objects.create(employee=employee, id_number=id_number)
            return redirect("create_idcard")
        except Employee.DoesNotExist:
            error = "Selected employee does not exist."
        except IntegrityError:
            error = "ID card for this employee already exists."
    return render(request, "create_id.html", {"employees": employees, "error": error})
