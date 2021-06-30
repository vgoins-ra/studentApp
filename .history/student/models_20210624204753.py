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
       ('FR', 'Freshman'),
       ('SOPH', 'Softmore'),
       ('JR', 'Junior'),
       ('SR', 'Senior'),
       ('UK', 'Unknown'),
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
    department = models.CharField(max_length = 100)
    grade = models.ForeignKey(Grade,related_name='student_grade', max_length = 50,default='UK', on_delete=models.SET_DEFAULT)
    school = models.CharField(blank=True,null=True,max_length = 100)

    def __str__(self):
        return self.fullname


#Create Certificate Table with relationship to Student Table (name and certificates)
class Certificate_Type(models.Model):
    CERT_VALUES = (
        ('None','0'),
        ('AWS Certified Solutions Architect','1'),
        ('AWS Certified Developer','2'),
        ('ScrumMaster','3'),
        ('Certified Information Systems Security Professional','4'),
        ('Certified in Risk and Information Systems Control','5'),
        ('Certified Ethical Hacker','6'),
        ('Citrix Certified Associate — Virtualization','7'),
        ('Google Certified Professional Cloud Architect','8'),
        ('IT project management','9'),
        ('Microsoft Certified Professionals Certifications','10')
    )
    certificate_type = models.CharField(blank=True,choices=CERT_VALUES,max_length = 100)

    def __str__(self):
        return self.certificate_type



#Create Certificate Table with relationship to Student Table (name and certificates)
class Certificates(models.Model):
    
    fullname = models.ForeignKey(Student,related_name='certif_student', max_length = 100, on_delete=models.CASCADE)
    certificate = models.ForeignKey(Certificate_Type,blank=True,max_length = 100,default='0',on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

