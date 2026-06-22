# models.py
from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
        
class Language(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Proficiency level (0-100)")
    
    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True)
    date_obtained = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class WorkExperience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class WorkResponsibility(models.Model):
    experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE, related_name='responsibilities')
    description = models.TextField()
    
    def __str__(self):
        return self.description[:50]

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, help_text="FontAwesome icon class", default="fas fa-code")
    
    def __str__(self):
        return self.title

class ProjectTechnology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='technologies')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} - {self.project.title}"

class Interest(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, help_text="FontAwesome icon class")
    
    def __str__(self):
        return self.name

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_name=100, null=True, blank=True)

    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(blank=True, null=True)
    about_me = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    
    def __str__(self):
        return f"Profile for {self.user.username}"

