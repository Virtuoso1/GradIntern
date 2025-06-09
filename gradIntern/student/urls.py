from django.urls import path
from . import views
app_name = 'student'
urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student-dashboard'),
    path('internship/<int:id>/', views.internship_detail, name='internship_detail'),
    path('internship/<int:id>/apply/', views.apply_internship, name='apply'),
    path('profile/', views.student_profile, name='student_profile'),

]
