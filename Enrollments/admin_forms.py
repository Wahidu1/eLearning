from django import forms
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['roll_number', 'course', 'status']
        widgets = {
            'roll_number' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'id' : "roll_number",
                }
            ),
            'course' : forms.Select(
                attrs={
                    'class' : 'form-select',
                    'id' : "course",
                }
            ),
            'status' : forms.Select(
                attrs={
                    'class' : 'form-select',
                    'id' : "status",
                }
            ),
        }