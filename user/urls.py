from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('usercreate/',views.usercreate,name='usercreate'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('login/',views.login,name='login'),

    path('userhome/',views.userhome,name='userhome'),
    path('admin-home/',views.adminhome,name='adminhome'),
    path('logout/',views.logout,name='logout'),

    path('profile/',views.profie,name='profile'),
    path('editpage/',views.editpage,name='editpage'),
    path('editdetails/<int:pk>',views.editdetails,name='editdetails'),

    path('coursepage/',views.coursepage,name='coursepage'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('studentpage/',views.studentpage,name='studentpage'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('showstudent/',views.showstd,name='showstd'),
    path('deletestd/<int:pk>',views.deletestd,name='deletestd'),
    path('showteacher/',views.showtchr,name='showtchr'),
    path('deletetchr/<int:pk>',views.deletetchr,name='deletetchr'),


    
]
