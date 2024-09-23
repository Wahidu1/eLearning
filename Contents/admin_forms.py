from django import forms
from .models import CommonPage, Contact, Testimonial

class CommonPageForm(forms.ModelForm):
    class Meta:
        model = CommonPage
        fields = ['name', 'title', 'image', 'key_point', 'description']
        widgets = {
            'name' : forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Enter Course Title',
                            'id': 'title',
                            'readonly' : 'True'
                        }),
            'title' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course Title',
                'id': 'title'
            }),
            'image' : forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course Title',
                'id': 'image'
            }),
            'key_point' : forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course Title',
                'id': 'key_point'
            }),
            'description' : forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course Title',
                'id': 'description'
            }),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['address', 'mobile', 'email']
        widgets = {
                'address' : forms.TextInput(
                    attrs={
                        'class' : 'form-control',
                        'placeholder' : "Enter address",
                        'id' : 'address'
                    }
                ),
                'mobile' : forms.TextInput(
                    attrs={
                        'class' : 'form-control',
                        'placeholder' : "Enter mobile",
                        'id' : 'mobile'
                    }
                ),
                'email' : forms.TextInput(
                    attrs={
                        'class' : 'form-control',
                        'placeholder' : "Enter email",
                        'id' : 'email'
                    }
                ),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'image', 'designation','description']
        widgets = {
                'name' : forms.TextInput(
                    attrs={
                        'class' : 'form-control',
                        'placeholder' : "Enter name",
                        'id' : 'name'
                    }
                ),
                'image' : forms.ClearableFileInput(
                    attrs={
                        'class' : 'form-control',
                        'placeholder' : "Enter Image",
                        'id' : 'image'
                    }
                ),
                'designation' : forms.TextInput(
                    attrs={
                        'class' : 'form-control',
                        'placeholder' : "Enter designation",
                        'id' : 'designation'
                    }
                ),
                'description' : forms.Textarea(
                    attrs={
                        'class' : 'form-control',
                        'placeholder' : "Enter description",
                        'id' : 'description',
                        'rows' : "4"
                    }
                ),
                
        }