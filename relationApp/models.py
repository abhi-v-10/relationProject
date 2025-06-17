from django.db import models

# OneToMany
class Doctor(models.Model):
    name = models.CharField(max_length=100)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

# ManyToMany
class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

# OneToOne
class Employee(models.Model):
    name = models.CharField(max_length=100)

class IDCard(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20)


