from django.urls import path
from . import views
app_name='clgapp'

urlpatterns = [

     path('',views.home,name="home"),
     path('register/',views.register,name="register"),
     path('login/',views.login,name="login"),
     path('student/', views.student, name="student"),



     path('add/',views.student_create_view,name="add"),

     path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
     path('logout/', views.log_out, name="logout"),
]