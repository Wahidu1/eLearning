from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentForm, LoginForm
from .models import CustomUser,Profile

def our_team_page(request):
    current_user = request.user
    try:
        instructors = CustomUser.objects.filter(role="instructor").select_related('profile')
    except CustomUser.DoesNotExist:
        instructors = None
    
    context = {
        "instructors": instructors,
        'current_page':"our_team",
        'current_user':current_user
    } 
    return render(request, "Accounts/frontend/our_team.html", context)

def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Save Successfully')
            return redirect("account:student_add")
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = StudentForm()

    return render(request, "Accounts/frontend/student-register.html", {'form': form})

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                student = CustomUser.objects.filter(username=username).first()
                if student.role ==  "student":
                    login(request, user)
                    return redirect("account:profile")
                else:
                    messages.error(request, 'You are not a student')
            else:
                messages.error(request, "User Not Found")
        else:
            messages.error(request, "Form is not valid")
    else:
        form = LoginForm()
    return render(request,"Accounts/frontend/login.html",{'form':form})


@login_required(login_url="/Accounts/login/")
def profile_page(request):
    current_user = request.user
    return render(request,"Accounts/frontend/profile.html",{'current_user':current_user})
