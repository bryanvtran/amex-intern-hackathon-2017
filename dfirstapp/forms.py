from django.forms import ModelForm

# Models
from .models import *

class StudentProfileForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name', 'email', 'bio', 'picture', 'resume']
