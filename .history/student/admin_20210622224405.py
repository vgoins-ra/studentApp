from django.contrib import admin
from .models import Certificates, Student, School, Grade, Department, Faculty

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Certificates)
admin.site.register(Grade)
admin.site.register(Department)
admin.site.register(Faculty)

