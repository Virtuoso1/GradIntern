from django import forms
from student.models import Student
from recruiter.models import Recruiter

class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password', 'location']
        widgets = {
            'password': forms.PasswordInput(),
        }
class RecruiterSignupForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = ['recruiter_name','company_name', 'email', 'phone_no', 'company_website', 'password', 'location']
        widgets = {
            'password': forms.PasswordInput(),
        }
