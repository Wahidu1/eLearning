from django.contrib import admin
from .models import Forum, Post, Message, Notification

admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Notification)
