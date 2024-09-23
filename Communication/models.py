from django.db import models

class Forum(models.Model):
    course = models.ForeignKey('Courses.Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Post(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    user = models.ForeignKey('Accounts.CustomUser', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.forum.title} - {self.created_at}"

class Message(models.Model):
    sender = models.ForeignKey('Accounts.CustomUser', related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey('Accounts.CustomUser', related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username} - {self.sent_at}"

class Notification(models.Model):
    USER_CHOICES = [
        ('single_student', 'Single Student'),
        ('single_instructor', 'Single Instructor'),
        ('all_student', 'All Student'),
        ('all_instructor', 'All Instructor'),
        ('all', 'All'),
    ]

    user = models.CharField(max_length=20, choices=USER_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Notification for {self.message}"
    
class NotificationReceivers(models.Model):
    user = models.ForeignKey('Accounts.CustomUser', related_name='notification_receivers', on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, related_name='notification_receivers', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.notification.created_at}"

