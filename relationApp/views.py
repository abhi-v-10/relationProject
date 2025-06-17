
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
            return redirect("home")
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
            Patient.objects.create(name=name, doctor_id=doctor_id)
            return redirect("home")
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
            return redirect("home")
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
            return redirect("home")
        except IntegrityError:
            error = "Error while creating student."
    return render(request, "create_student.html", {"courses": courses, "error": error})

def create_employee(request):
    error = None
    if request.method == "POST":
        name = request.POST.get("name")
        try:
            Employee.objects.create(name=name)
            return redirect("home")
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

            IDCard.objects.create(employee_id=employee_id, id_number=id_number)
            return redirect("home")
        except Employee.DoesNotExist:
            error = "Selected employee does not exist."
        except IntegrityError:
            error = "ID card for this employee already exists."
    return render(request, "create_id.html", {"employees": employees, "error": error})


def view_doctors_patients(request):
    doctors = Doctor.objects.prefetch_related('patient_set')
    return render(request, "doctor_patient.html", {"doctors": doctors})

def view_courses_students(request):
    students = Student.objects.prefetch_related('courses')
    return render(request, "course_students.html", {"students": students})

def view_employees_idcards(request):
    employees = Employee.objects.select_related('idcard')
    return render(request, "employee_idcards.html", {"employees": employees})
