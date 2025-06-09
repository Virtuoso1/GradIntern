from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .forms import StudentSignupForm, RecruiterSignupForm
from django.contrib.auth.hashers import make_password, check_password
from student.models import Student
from recruiter.models import Recruiter

def general(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def student_login(request):
    error = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(email__iexact=email)
            if check_password(password, student.password):
                request.session['student_id'] = student.id
                request.session['student_name'] = student.name
                return redirect('student:student-dashboard') 
            else:
                error = 'Invalid password'
        except Student.DoesNotExist:
            error = 'Email not registered'

    return render(request, 'student-login.html', {'error': error})

def recruiter_login(request):
    error = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            recruiter = Recruiter.objects.get(email=email)
            if check_password(password, recruiter.password):
                request.session['recruiter_id'] = recruiter.id
                request.session['recruiter_name'] = recruiter.recruiter_name
                return redirect('recruiter:recruiter-dashboard')
            else:
                error = 'Invalid password'
        except Recruiter.DoesNotExist:
            error = 'Email not registered'

    return render(request, 'recruiter-login.html', {'error': error})

def recruiter_signup(request):
    if request.method == 'POST':
        form = RecruiterSignupForm(request.POST)
        if form.is_valid():
            recruiter = form.save(commit=False)
            recruiter.password = make_password(form.cleaned_data['password'])
            recruiter.save()
            return redirect('recruiter_login')
    else:
        form = RecruiterSignupForm()
    return render(request, 'recruiter-signup.html', {'form': form})

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.password = make_password(form.cleaned_data['password'])
            student.save()
            return redirect('student_login')
    else:
        form = StudentSignupForm()
    return render(request, 'student-signup.html', {'form': form})