from django.contrib import admin
from .models import Certificates, Student, School, Grade, Department, Faculty, Certificate_Type

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Certificates)
admin.site.register(Grade)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Certificate_Type)

