from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    course=CourseModel.objects.all()
    context={'course': course}
    return render(request,'signup.html',context)

def usercreate(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        uname=request.POST['username']
        age=request.POST['age']
        email=request.POST['email']
        gender=request.POST['gender']
        dob=request.POST['dob']
        phoneno=request.POST['number']
        address=request.POST['address']
        password1=request.POST['password']
        password2=request.POST['cpassword']
        course=request.POST['select']
        # if request.FILES.get('image') is not None:
        photo=request.FILES.get('image')
        # else:
        #     photo='static/default.png' 

        if password1==password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username already exists')
                return redirect('signup')   
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists') 
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=password1)
                user.save()

                data=User.objects.get(id=user.id)
                cdata=CourseModel.objects.get(id=course)
                ext_user_data=TeacherModel(Address=address,Age=age,Gender=gender,Image=photo,DOB=dob,Mobile=phoneno,Teacher=data,Course=cdata)
                ext_user_data.save()
                messages.success(request,'Profile Registered')
                return redirect('loginpage')
        else:
            messages.info(request,'Password is not matching')
            return redirect('signup')    

def loginpage(request):
    return render(request,'login.html') 

def login(request):
    if request.method=='POST':
        username=request.POST['username'] 
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('adminhome')
            else:
                auth.login(request,user)
                messages.info(request,f'Welcome {username}')
                return redirect('userhome') 
        else:
            messages.warning(request,'Something Wrong...')
            return redirect('loginpage')    

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')            

@login_required(login_url='login')
def userhome(request):
    return render(request,'user/user_home.html')


@login_required(login_url='login')
def adminhome(request):
    return render(request,'administration/admin_home.html')

def profie(request):
    teacher=TeacherModel.objects.get(Teacher=request.user)
    context={'users': teacher}
    return render(request,'user/profile.html',context)

def editpage(request):
    teacher=TeacherModel.objects.get(Teacher=request.user)
    course=CourseModel.objects.all()
    context={'edit': teacher,'course': course}
    return render(request,'user/editprofile.html',context)


def editdetails(request,pk):
    if request.method=='POST':
        
        teacher=TeacherModel.objects.get(id=pk)
        user_id=teacher.Teacher.id
        user=User.objects.get(id=user_id)
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.username=request.POST.get('username')
        user.email=request.POST.get('email')
        teacher.Gender=request.POST.get('gender')
        teacher.DOB=request.POST.get('dob')
        teacher.Age=request.POST.get('age')
        teacher.Mobile=request.POST.get('number')
        teacher.Address=request.POST.get('address')
        old=teacher.Image
        new=request.FILES.get('files')
        if old != None and new==None:
            teacher.Image=old
        else:
            teacher.Image=new 
        select=request.POST.get('select')
        course=CourseModel.objects.get(id=select)
        teacher.Course=course   
     

        teacher.save()
        user.save()
        
        
        return redirect('profile')


@login_required(login_url='login')
def coursepage(request):
    return render(request,'administration/course.html')

def addcourse(request):
    if request.method=='POST':
        course_name=request.POST['coursename']
        course=CourseModel(course_name=course_name)
        course.save()
        return redirect('adminhome')

@login_required(login_url='login')
def studentpage(request):
    course=CourseModel.objects.all()
    context={'course': course}
    return render(request,'administration/students.html',context)

def addstudent(request):
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        age=request.POST['age']
        select=request.POST['select']
        course=CourseModel.objects.get(id=select)
        student=StudentModel(name=name,address=address,age=age,Course=course)
        student.save()
        return redirect('adminhome')
    
def showstd(request):
    if not request.user.is_staff:
        return redirect('loginpage')
    students=StudentModel.objects.all()
    context={'students':students}
    return render(request,'administration/showstd.html',context)    

def deletestd(request,pk):
    if not request.user.is_staff:
        return redirect('loginpage')
    student=StudentModel.objects.get(id=pk)
    student.delete()
    return redirect('showstd')

def showtchr(request):
    if not request.user.is_staff:
        return redirect('loginpage')
    teachers=TeacherModel.objects.all()
    context={'teachers':teachers}
    return render(request,'administration/showtchr.html',context)  

def deletetchr(request,pk):
    if not request.user.is_staff:
        return redirect('loginpage')
    teacher=TeacherModel.objects.get(id=pk)
    user_id=teacher.Teacher.id
    user=User.objects.get(id=user_id)
    teacher.delete()
    user.delete()
    return redirect('showtchr')  
