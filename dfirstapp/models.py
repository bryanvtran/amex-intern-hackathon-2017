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
    picture = models.ImageField(upload_to='uploads/pictures/')
    resume = models.FileField(upload_to='uploads/resumes/')

class StudentInterest(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    interest = models.CharField(max_length=50)

class StudentSkill(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)

class StudentLinks(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    url = models.URLField()

# """
# TeamProfile
# """
# class TeamProfile(models.Model):
#     name = models.StringField(max_length=30)
#     picture
#     description
#     required_skills
#
# """
# TeamMembers
# """
# class TeamMembers(models.Model):
#     name
#     email
#     bio
