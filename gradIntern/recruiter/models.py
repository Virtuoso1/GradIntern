from django.db import models

class Recruiter(models.Model):
    recruiter_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=20)
    company_website = models.CharField()
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.location:
            self.location = self.location.upper()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.recruiter_name

class Internship(models.Model):
    title = models.CharField(max_length=255)
    internship_description = models.TextField()
    stipend = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    skills_required = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
