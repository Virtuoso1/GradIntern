from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name ='general'),
    path('Slogin/', views.student_login, name='student_login'),
    path('Ssignup/', views.student_signup, name='student_signup'),
    path('Rlogin/', views.recruiter_login, name='recruiter_login'),
    path('Rsignup/', views.recruiter_signup, name='recruiter_signup'),
    path('student-signup/', views.student_signup, name='student-signup'),

]