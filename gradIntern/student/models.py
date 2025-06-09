from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  
    location = models.CharField(max_length=255)
    # to be filled later
    phone_no = models.CharField(max_length=20, blank=True)
    university = models.CharField(max_length=255, blank=True)
    skill_description = models.TextField(blank=True)
    cv_url = models.FileField(upload_to='cv_uploads/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.location:
            self.location = self.location.upper()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    application_status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Applied')
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    internship = models.ForeignKey('recruiter.Internship', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} applied to {self.internship.title}"
