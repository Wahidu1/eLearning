from django.db import models

class Enrollment(models.Model):
    roll_number = models.CharField(max_length=20, null=True)
    course = models.ForeignKey('Courses.Course', on_delete=models.CASCADE, related_name='enrollment')
    status = models.CharField(max_length=10, choices=(('active', 'Active'), ('completed', 'Completed'), ('dropped', 'Dropped')))
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"

class Waitlist(models.Model):
    student = models.ForeignKey('Accounts.CustomUser', on_delete=models.CASCADE)
    course = models.ForeignKey('Courses.Course', on_delete=models.CASCADE)
    waitlist_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f"{self.student.username} - {self.course.title} (Waitlist)"