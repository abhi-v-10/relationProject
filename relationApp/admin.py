from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(IDCard)