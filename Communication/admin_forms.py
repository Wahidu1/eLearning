from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['user', 'message']
        widgets = {
            'user' : forms.Select(
                attrs={
                    'class' : 'form-select',
                    'id' : "user",
                    'selected' : "Open this select menu"
                }
            ),
            'message' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : "Enter message",
                    'id' : "message",
                    'rows' : "4"
                }
            ),

        }