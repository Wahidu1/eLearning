from django.db import models

class Progress(models.Model):
    student = models.ForeignKey('Accounts.CustomUser', on_delete=models.CASCADE)
    course = models.ForeignKey('Courses.Course', on_delete=models.CASCADE)
    percentage_completion = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    milestones = models.TextField(blank=True, null=True)  # To store milestones as JSON or comma-separated values
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.title} Progress"

class Achievement(models.Model):
    student = models.ForeignKey('Accounts.CustomUser', on_delete=models.CASCADE)
    course = models.ForeignKey('Courses.Course', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_awarded = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
        
    def __str__(self):
        return f"{self.student.username} - {self.name}"