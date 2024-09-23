from django import forms
from django.utils import timezone
from .models import CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm

class StudentForm(UserCreationForm):
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter bio'}),
        required=True
    )
    profile_picture = forms.ImageField(
        label='Image', 
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    contact_details = forms.CharField(
        max_length=255,
        label='Contact',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
        required=True
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
        required=False
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
        required=False
    )
    

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }

    def generate_user_id(self):
        current_year = timezone.now().year
        count = CustomUser.objects.count() + 1
        return f"{current_year}{count:05d}"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'
        if not user.pk:
            roll = self.generate_user_id()
        else:
            roll = user.profile.roll 
            
        if commit:
            user.save()

            profile, created = Profile.objects.get_or_create(user=user)
            profile.bio = self.cleaned_data['bio']
            profile.profile_picture = self.cleaned_data['profile_picture']
            profile.contact_details = self.cleaned_data['contact_details']
            profile.roll = roll
            profile.save()
        
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
        required=True
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
        required=True
    )