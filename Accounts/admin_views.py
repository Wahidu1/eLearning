from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .admin_forms import LoginForm, InstructorForm, StudentForm
from .models import CustomUser, Profile

def backend_login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,password=password)
            if user:
                login(request,user)
                return redirect("backend_home:backend_dashboard")
            
    else:
        form = LoginForm()
    return render(request, "Accounts/backend/login.html", {'form':form})

def backend_instructor_add(request):
    if request.method == "POST":
        form = InstructorForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_account:backend_instructor_add")
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = InstructorForm()

    return render(request, "Accounts/backend/instructor-add.html", {'form': form})

def backend_instructor_edit(request,id):
    instructor = get_object_or_404(CustomUser, id=id)
    profile = get_object_or_404(Profile, user=instructor)

    if request.method == "POST":
        form = InstructorForm(request.POST, request.FILES,instance=instructor)
        if form.is_valid():
            user = form.save(commit=False)
            profile.bio = form.cleaned_data['bio']
            profile.contact_details = form.cleaned_data['contact_details']
            if form.cleaned_data['profile_picture']:
                profile.profile_picture = form.cleaned_data['profile_picture']
            user.save()
            profile.save()                
            
            messages.success(request, 'Update Successfully')
            return redirect("backend_account:backend_instructor_edit", id=instructor.id)
        else:
            messages.error(request, 'Update NOt Successfully!!')
  
    else:
        initial_data = {
            'bio': profile.bio,
            'contact_details': profile.contact_details,
            'profile_picture': profile.profile_picture
        }
        form = InstructorForm(instance=instructor, initial=initial_data)
    return render(request, "Accounts/backend/instructor-edit.html", {'form':form})

def backend_instructor_list(request):
    instructors = CustomUser.objects.filter(role='instructor').select_related('profile')
    return render(request, "Accounts/backend/instructor-list.html", {'instructors':instructors})

def backend_instructor_delete(request,id):
    return HttpResponse("Not Available Now")
    instructor = get_object_or_404(CustomUser, id=id)
    profile = get_object_or_404(Profile, user=instructor)
    instructor.delete()
    profile.delete()
    return redirect("backend_account:backend_instructor_list")

def backend_student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_account:backend_student_add")
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = StudentForm()

    return render(request, "Accounts/backend/student-add.html", {'form': form})

def backend_student_edit(request, id):
    student = get_object_or_404(CustomUser, id=id)
    profile = get_object_or_404(Profile, user=student)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            user = form.save(commit=False)
            profile.bio = form.cleaned_data['bio']
            profile.contact_details = form.cleaned_data['contact_details']
            if form.cleaned_data['profile_picture']:
                profile.profile_picture = form.cleaned_data['profile_picture']
            user.save()
            profile.save()

            messages.success(request, 'Update Successfully')
            return redirect("backend_account:backend_student_edit", id=student.id)
        else:
            messages.error(request, 'Update Not Successfully!!')
    else:
        initial_data = {
            'bio': profile.bio,
            'contact_details': profile.contact_details,
            'profile_picture': profile.profile_picture
        }
        form = StudentForm(instance=student, initial=initial_data)
    
    return render(request, "Accounts/backend/student-edit.html", {'form': form})

def backend_student_list(request):
    students = CustomUser.objects.filter(role='student').select_related('profile')
    return render(request, "Accounts/backend/student-list.html", {'students':students})

def backend_student_delete(request,id):
    return HttpResponse("Not Available Now")
    student = get_object_or_404(CustomUser, id=id)
    profile = get_object_or_404(Profile, user=student)
    student.delete()
    profile.delete()
    return redirect("backend_account:backend_student_list")

def get_student_info(request, roll_number):
    # student = get_object_or_404(CustomUser, roll_number=roll_number)
    student_info = get_object_or_404(Profile, roll=roll_number)
    data = {
        'name': student_info.user.last_name,
        'email': student_info.user.email,
        'phone': student_info.contact_details,
        'image': student_info.profile_picture.url,

        # Add other fields if needed
    }
    return JsonResponse(data)