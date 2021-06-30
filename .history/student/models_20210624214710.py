from django.db import models
from django.db.models.fields import CharField
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from datetime import datetime 

#Create School Table with relationship to Student Table (school) 
class School(models.Model):
    school =  models.CharField(max_length = 100)

    def __str__(self):
        return self.school


# Create Faculty Table with relationship to Department Table (department)
class Faculty(models.Model): 
    faculty = models.CharField(max_length = 100)
    school_assigned = models.ForeignKey(School,blank=True,null=True, on_delete=CASCADE)

    def __str__(self):
        return self.faculty


#Create Department Table with relationship to Student Table (faculty)
class Department(models.Model): 
    DEPT_VALUES = (
        ('Computer Science','Computer Science'),
        ('Business Administration','Business Administration'),
        ('International Studies','International Studies'),
        ('Natural Sciences','Natural Sciences'),
    )
    name = models.CharField(choices=DEPT_VALUES,max_length = 100)
    faculty = models.ForeignKey(Faculty,blank=True,null=True, on_delete=CASCADE)

    def __str__(self):
        return self.name 


#Create Grade Table with relationship to Student Table (grade)
class Grade(models.Model):
    GRADE_VALUES = (
       ('FRESHMAN', 'Freshman'),
       ('SOPHMORE', 'Sophmore'),
       ('JUNIOR', 'Junior'),
       ('SENIOR', 'Senior'),
       ('UKNOWN', 'Unknown'),
    )  
    grade = models.CharField(max_length = 50,choices=GRADE_VALUES, blank=True)
       
    def __str__(self):
        return self.grade


# Create Student Table which relationship is one of many tables above
class Student(models.Model):
    GRAD_YEARS = (
        ('2021','2021'),
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),
        ('2026','2026'),
        ('2027','2027'),
        ('2028','2028'),
        ('Unknown', 'Unknown'),
    )

    fullname = models.CharField(max_length = 100)
    year_of_graduation = models.CharField(blank=True,max_length=15,choices=GRAD_YEARS)
    department = models.ForeignKey(Department,related_name='student_dept', max_length = 100,on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade,related_name='student_grade', max_length = 50,default='UNKNOWN',on_delete=models.SET_DEFAULT)
    school = models.ForeignKey(School,related_name='student_school', max_length = 100,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


#Create Certificate Table with relationship to Student Table (name and certificates)
class Certificate_Type(models.Model):
    CERT_VALUES = (
        ('None','None'),
        ('AWS Certified Solutions Architect','AWS Certified Solutions Architect'),
        ('AWS Certified Developer','AWS Certified Developer'),
        ('ScrumMaster','ScrumMaster'),
        ('Certified Information Systems Security Professional','Certified Information Systems Security Professional'),
        ('Certified in Risk and Information Systems Control','Certified in Risk and Information Systems Control'),
        ('Certified Ethical Hacker','Certified Ethical Hacker'),
        ('Citrix Certified Associate — Virtualization','Citrix Certified Associate — Virtualization'),
        ('Google Certified Professional Cloud Architect','Google Certified Professional Cloud Architect'),
        ('IT project management','IT project management'),
        ('Microsoft Certified Professionals Certifications','Microsoft Certified Professionals Certifications')
    )
    certificate_type = models.CharField(blank=True,choices=CERT_VALUES,max_length = 100)

    def __str__(self):
        return self.certificate_type



#Create Certificate Table with relationship to Student Table (name and certificates)
class Certificates(models.Model):
    
    fullname = models.ForeignKey(Student,related_name='certif_student', max_length = 100, on_delete=models.CASCADE)
    certificate = models.ForeignKey(Certificate_Type,blank=True,max_length = 100,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

