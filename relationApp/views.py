
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorSerializer, PatientSerializer, CourseSerializer, StudentSerializer, EmployeeSerializer, IDCardSerializer


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


@api_view(['GET', 'POST'])
def api_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def api_patients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def api_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def api_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            if 'courses' in request.data:
                student.courses.set(request.data['courses'])
            return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def api_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def api_idcards(request):
    if request.method == 'GET':
        idcards = IDCard.objects.all()
        serializer = IDCardSerializer(idcards, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IDCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def api_employees_with_idcards(request):
    employees = Employee.objects.select_related('idcard')
    data = []

    for emp in employees:
        try:
            idcard = emp.idcard
            idcard_data = IDCardSerializer(idcard).data
        except IDCard.DoesNotExist:
            idcard_data = None

        data.append({
            "employee": EmployeeSerializer(emp).data,
            "idcard": idcard_data
        })

    return Response(data)


@api_view(['GET'])
def api_doctors_with_patients(request):
    data = []
    for doctor in Doctor.objects.prefetch_related('patient_set'):
        data.append({
            'doctor': DoctorSerializer(doctor).data,
            'patients': PatientSerializer(doctor.patient_set.all(), many=True).data
        })
    return Response(data)

@api_view(['GET'])
def api_courses_with_students(request):
    data = []
    for course in Course.objects.prefetch_related('student_set'):
        data.append({
            'course': CourseSerializer(course).data,
            'students': StudentSerializer(course.student_set.all(), many=True).data
        })
    return Response(data)


