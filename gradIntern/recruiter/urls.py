from django.urls import path
from . import views

app_name = 'recruiter'

urlpatterns = [
    path('dashboard/', views.recruiter_dashboard, name='recruiter-dashboard'),
    path('create-internship/', views.create_internship, name='create_internship'),
    path('internship/<int:internship_id>/applicants/', views.view_applicants, name='view_applicants'),
    path('application/<int:application_id>/detail/', views.view_applicant_detail, name='view_applicant_detail'),

]
