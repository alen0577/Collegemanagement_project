from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CourseModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','course_name')

@admin.register(TeacherModel)
class TeacherDetailAdmin(admin.ModelAdmin):
    list_display=('id','Address','Gender')   

@admin.register(StudentModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','name')    