from django.shortcuts import get_object_or_404, render,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Category,Course,Module, Resource
from Accounts.models import CustomUser, Profile
from Contents.models import Testimonial
from Enrollments.models import Enrollment

def dashboard(request):
    current_user = request.user

    categories = Category.objects.all()
    courses = Course.objects.all()[:3]
    instructors = CustomUser.objects.filter(role="instructor")
    testimonials = Testimonial.objects.all()
    data = {
        'categories': categories,
        "courses":courses,
        'instructors':instructors,
        'testimonials':testimonials,
        'current_page':"dashboard",
        'current_user':current_user

    }
    return render(request, "Courses/frontend/dashboard.html",data)

def course_category_details(request,id):
    current_user = request.user

    category = Category.objects.filter(id=id).first()
    courses = Course.objects.filter(category=category)
    context = {
        'courses':courses,
        "category":category,
        'current_user':current_user

        }
    return render(request, "Courses/frontend/course_category_details.html",context )

def course_details(request,id):
    current_user = request.user

    course = Course.objects.filter(id=id).first()
    modules = Module.objects.filter(course=course)
    context = {
        'course':course,
        'modules':modules,
        'current_user':current_user
        }
    return render(request, "Courses/frontend/course_details.html", context)

def course_page(request):
    current_user = request.user

    categories = Category.objects.all()
    courses = Course.objects.all()[:3]
    context = {
        'categories': categories,
        "courses":courses,
        'current_page':"course",
        'current_user':current_user

    }
    return render(request, "Courses/frontend/course_page.html", context)

def my_course_page(request):
    current_user = request.user
    roll = current_user.profile.roll
    print(roll)
    enrollments = Enrollment.objects.select_related('course').filter(roll_number=roll)

    # Iterate over the queryset to access each enrollment and its associated course
    courses = []
    for enrollment in enrollments:
        course = enrollment.course
        courses.append(course)
    context = {
        'courses':courses,
        'current_page':"my_course",
        'current_user':current_user

    }
    return render(request, "Courses/frontend/my-course.html", context)

@login_required(login_url="/Accounts/login/")

def course_module(request,id):
    current_user = request.user
    course = Course.objects.filter(id=id).first()
    modules = Module.objects.filter(course__id=id)
    module_with_resource = []

    for module in modules:
        resources = Resource.objects.filter(module=module)
        module_with_resource.append({
            'module': module,
            'resources': resources
        })
   
    # print(module_with_resource)
    context = {
        'course':course,
        'modules':modules,
        'current_page':"my_course",
        'current_user':current_user,
        'module_with_resource':module_with_resource

    }
    return render(request, "Courses/frontend/course-module.html", context)

    

