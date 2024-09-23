from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/',null=True)
    designation = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name
    
class CommonPage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    title = models.CharField(max_length=255, verbose_name="Title")
    image = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name="Image")
    key_point  = models.TextField(verbose_name="Point")
    description = models.TextField(verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    # class Meta:
    #     verbose_name = "About"
    #     verbose_name_plural = "About"

    def __str__(self):
        return self.title


class Contact(models.Model):
    address = models.CharField(max_length=255, verbose_name="address")
    mobile = models.CharField(max_length=255, verbose_name="mobile")
    email = models.CharField(max_length=255, verbose_name="email")
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

class Query(models.Model):
    name = models.CharField(max_length=255, verbose_name="address")
    email = models.CharField(max_length=255, verbose_name="email")
    subject = models.CharField(max_length=255, verbose_name="subject")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

