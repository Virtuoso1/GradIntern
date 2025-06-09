from django import forms
from .models import Internship

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ['title', 'internship_description', 'stipend', 'location', 'skills_required']
        widgets = {
            'internship_description': forms.Textarea(attrs={'rows': 4}),
            'skills_required': forms.Textarea(attrs={'rows': 3}),
        }
    def clean_location(self):
        location = self.cleaned_data['location']
        return location.upper()
