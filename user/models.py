from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CourseModel(models.Model):
    course_name=models.CharField(max_length=100)

class TeacherModel(models.Model):
    Teacher=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    Address=models.CharField(max_length=200)
    Gender=models.CharField(max_length=20)
    Age=models.IntegerField()
    Image=models.ImageField(null=True,blank=True,upload_to='image/') 
    DOB=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100) 

class StudentModel(models.Model):
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    age=models.IntegerField()
    join_date=models.DateTimeField(auto_now_add=True)
