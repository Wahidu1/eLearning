from django import forms
from .models import Category, Course, Module, Resource
 
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course Category',
                'id': 'title'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'image'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description here',
                'id': 'description',
                'style': 'height: 150px'
            }),
        }
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor','category','price', 'image', 'start_date','end_date',]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course Title',
                'id': 'title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course Description',
                'id': 'description',
                'rows':4
            }),
            'instructor': forms.Select(attrs={
                'class': 'form-control',
                'id': 'instructor'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'id': 'category'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Course Price',
                'id': 'price'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'image'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type':'date',
                'id': 'start_date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'end_date'
            }),
        }

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'description','course']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Module Title',
                'id': 'title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Module Description',
                'id': 'description',
                'rows':4
            }),
            'course': forms.Select(attrs={
                'class': 'form-control',
                'id': 'course'
            }),
        } 
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['module','title','resource_type','link','file']
        widgets = {
            'module': forms.Select(attrs={
                'class': 'form-control',
                'id': 'module'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Resource Title',
                'id': 'title'
            }),
            'resource_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Resource Type',
                'id': 'description',
                'rows':4
            }),
            'link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Resource Link',
                'id': 'link'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'file'
            }),
        } 