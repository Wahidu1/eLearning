from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Notification
from .admin_forms import NotificationForm
from django.contrib import messages

def notification_add(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Add Successfully")
        else:
            messages.error(request,"Something is wrong")
    else:
        form = NotificationForm(initial={'user': 'default_user_id'})

    return render(request, "Communication/backend/notification-add.html",{"form":form})


def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, "Communication/backend/notification-list.html",{"notifications":notifications})
