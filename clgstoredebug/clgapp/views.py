from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from .forms import StudentCreationForm
from .models import student,course

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('clgapp:register')

            user = User.objects.create_user(username=username, password=password)
            user.save()

            messages.success(request, 'Registration successful. Please log in.')
            return redirect('clgapp:login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('clgapp:register')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('clgapp:student')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('clgapp:login')

    return render(request, 'login.html')
def student(request):
    return render(request, 'student.html')
def add(request):
    return render(request, 'add.html')


def student_create_view(request):
    form = StudentCreationForm()
    if request.method=='POST':
        form=StudentCreationForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Submission successful')
        return redirect('clgapp:add')
    return render(request, 'add.html', {'form': form})

def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = course.objects.filter(department_id=department_id).all()
    return render(request, 'clgapp/courses.html', {'courses': courses})


def log_out(request):
    logout(request)
    return HttpResponse("logout successfully")
