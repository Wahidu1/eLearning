from django.db import models


class CourseAnalytics(models.Model):
    course = models.ForeignKey('Courses.Course', on_delete=models.CASCADE)
    total_enrollments = models.PositiveIntegerField(default=0)
    total_completions = models.PositiveIntegerField(default=0)
    average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f"Analytics for {self.course.title}"

class UserAnalytics(models.Model):
    user = models.ForeignKey('Accounts.CustomUser', on_delete=models.CASCADE)
    total_logins = models.PositiveIntegerField(default=0)
    courses_enrolled = models.PositiveIntegerField(default=0)
    courses_completed = models.PositiveIntegerField(default=0)
    average_quiz_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    last_login = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f"Analytics for {self.user.username}"

