from __future__ import unicode_literals

from django.db import models

# Create your models here.
"""
StudentProfile
"""
class StudentProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField()
    picture = models.ImageField(upload_to='uploads/pictures/', null=True, blank=True)
    resume = models.FileField(upload_to='uploads/resumes/', null=True, blank=True)

class StudentInterest(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    interest = models.CharField(max_length=50)

class StudentSkill(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)

class StudentLink(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    url = models.URLField()

"""
TeamProfile
"""
class TeamProfile(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='uploads/pictures/', null=True, blank=True)
    description = models.TextField()

class TeamSkill(models.Model):
    team = models.ForeignKey(TeamProfile, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)

class TeamMember(models.Model):
    team = models.ForeignKey(TeamProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField()
