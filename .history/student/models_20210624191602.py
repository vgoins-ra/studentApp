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
    name = models.CharField(max_length = 100)
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
    fullname = models.CharField(max_length = 100)
    year_of_graduation = models.DateField(blank=True,max_length=15, default=datetime.now().year)
    department = models.CharField(max_length = 100)
    grade = models.ForeignKey(Grade,related_name='student_grade', max_length = 50,default='UK', on_delete=models.SET_DEFAULT)
    school = models.CharField(blank=True,null=True,max_length = 100)

    def __str__(self):
        return self.fullname


#Create Certificate Table with relationship to Student Table (name and certificates)
class Certificate_Type(models.Model):
    CERT_VALUES = (
        ('None'),
        ('AWS Certified Solutions Architect'),
        ('AWS Certified Developer'),
        ('ScrumMaster'),
        ('Certified Information Systems Security Professional'),
        ('Certified in Risk and Information Systems Control'),
        ('Certified Ethical Hacker'),
        ('Citrix Certified Associate — Virtualization'),
        ('Google Certified Professional Cloud Architect'),
        ('IT project management'),
        ('Microsoft Certified Professionals Certifications')
    )
    certificate_type = models.CharField(blank=True,choices=CERT_VALUES,max_length = 100)

    def __str__(self):
        return self.certificate_type



#Create Certificate Table with relationship to Student Table (name and certificates)
class Certificates(models.Model):
    CERT_VALUES = (
        ('0','None'),
        ('1','AWS Certified Solutions Architect'),
        ('2','AWS Certified Developer'),
        ('3','ScrumMaster'),
        ('4','Certified Information Systems Security Professional'),
        ('5','Certified in Risk and Information Systems Control'),
        ('6','Certified Ethical Hacker'),
        ('7','Citrix Certified Associate — Virtualization'),
        ('8','Google Certified Professional Cloud Architect'),
        ('9','IT project management'),
        ('10','Microsoft Certified Professionals Certifications')
    )
    fullname = models.ForeignKey(Student,related_name='certif_student', max_length = 100, on_delete=models.CASCADE)
    certificate = models.CharField(blank=True,choices=CERT_VALUES,default='0',max_length = 100)

    def __str__(self):
        return self.certificate

