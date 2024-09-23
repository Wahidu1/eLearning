from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = (
        ('student','Student'),
        ('instructor','Instructor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10,choices=ROLES)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(blank=True)
    roll = models.CharField(blank=True,max_length=10,unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True)
    contact_details = models.CharField(max_length=255,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.user.username