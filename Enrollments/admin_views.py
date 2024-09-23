from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Enrollment
from .admin_forms import EnrollmentForm
from django.contrib import messages

def enrollment_add(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Add Successfully")
        else:
            messages.error(request,"Something is wrong")
    else:
        form = EnrollmentForm(initial={'user': 'default_user_id'})

    return render(request, "Enrollments/backend/enrollment-add.html",{"form":form})


def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, "Enrollments/backend/enrollment-list.html",{"enrollments":enrollments})
