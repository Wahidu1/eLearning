from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/',null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey("Accounts.CustomUser", limit_choices_to={"role":"instructor"}, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    price = models.IntegerField(default=0,null=True)
    image = models.ImageField(upload_to='img/',null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title

class Resource(models.Model):
    module = models.ForeignKey(Module,  on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=50)
    link = models.URLField(blank=True)
    file = models.FileField(upload_to='resources/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title
    
    
    
