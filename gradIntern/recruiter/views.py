from django.shortcuts import render, redirect, get_object_or_404
from .forms import InternshipForm
from .models import Internship
from student.models import Application
from django.contrib import messages
def recruiter_dashboard(request):
    recruiter_id = request.session.get('recruiter_id')
    if not recruiter_id:
        return redirect('recruiter_login')
    internships = Internship.objects.filter(recruiter_id=recruiter_id).order_by('-posted_date')
    return render(request, 'dashboard.html', {'internships': internships})

def create_internship(request):
    recruiter_id = request.session.get('recruiter_id')
    if not recruiter_id:
        return redirect('recruiter:recruiter_login')

    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            internship = form.save(commit=False)
            internship.recruiter_id = recruiter_id  
            internship.save()
            return redirect('recruiter:recruiter-dashboard')
    else:
        form = InternshipForm()
    
    return render(request, 'new-internship.html', {'form': form})

def view_applicants(request, internship_id):
    if 'recruiter_id' not in request.session:
        return redirect('recruiter_login')

    internship = get_object_or_404(Internship, id=internship_id, recruiter_id=request.session['recruiter_id'])
    applications = Application.objects.filter(internship=internship).select_related('student')

    return render(request, 'view-applicants.html', {
        'internship': internship,
        'applications': applications
    })


def view_applicant_detail(request, application_id):
    if 'recruiter_id' not in request.session:
        return redirect('recruiter_login')

    application = get_object_or_404(Application, id=application_id, internship__recruiter_id=request.session['recruiter_id'])
    student = application.student

    if request.method == 'POST':
        action = request.POST.get('action')
        if action in ['Accepted', 'Rejected']:
            application.application_status = action
            application.save()
            messages.success(request, f"Application has been {action.lower()}.")
            return redirect('recruiter:view_applicants', internship_id=application.internship.id)

    return render(request, 'applicant-details.html', {
        'application': application,
        'student': student,
    })