from django.shortcuts import render, redirect, get_object_or_404
from recruiter.models import Internship
from .models import Student, Application
from django.contrib import messages

def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student-login')
    internships = Internship.objects.all().order_by('-posted_date')
    return render(request, 'sdashboard.html', {'internships': internships})

def internship_detail(request, id):
    internship = get_object_or_404(Internship, id=id)
    return render(request, 'student-listing-detail.html', {'internship': internship})

def apply_internship(request, id):
    if request.method == 'POST':
        if 'student_id' not in request.session:
            return redirect('general:student_login')

        internship = get_object_or_404(Internship, id=id)
        student_id = request.session.get('student_id')

        if Application.objects.filter(student_id=student_id, internship=internship).exists():
            messages.error(request, "You already applied to this internship.")
        else:
            Application.objects.create(student_id=student_id, internship=internship)
            messages.success(request, "Application submitted successfully.")

        return redirect('student:internship_detail', id=id)

def student_profile(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = get_object_or_404(Student, id=request.session['student_id'])

    if request.method == 'POST':
        student.student_name = request.POST.get('student_name')
        student.phone_no = request.POST.get('phone_no')
        student.university = request.POST.get('university')
        student.location = request.POST.get('location').upper()
        student.skill_description = request.POST.get('skill_description')

        if 'cv' in request.FILES:
            student.cv = request.FILES['cv']
        student.save()
        messages.success(request, 'Profile updated successfully.')

    applications = Application.objects.filter(student=student).select_related('internship')

    return render(request, 'student-profile.html', {
        'student': student,
        'applications': applications
    })