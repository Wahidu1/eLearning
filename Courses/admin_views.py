from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import Category,Course,Module, Resource
from .admin_forms import CategoryForm, CourseForm, ModuleForm, ResourceForm
from django.contrib import messages

def course_category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_course:course_category_add")
        
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = CategoryForm()
    return render(request, "Courses/backend/course-category-add.html",{'form':form})

def course_category_list(request):
    categories = Category.objects.all()
    return render(request, "Courses/backend/course-category-list.html",{'categories':categories})


def course_category_edit(request,id):
    course_category = get_object_or_404(Category,id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES,instance=course_category)

        if form.is_valid():
            form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_course:course_category_add")
        
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = CategoryForm(instance=course_category)
    return render(request, "Courses/backend/course-category-edit.html",{'form':form})


def course_category_delete(request,id):
    course_category = get_object_or_404(Category,id=id)
    course_category.delete()
    return redirect("backend_course:course_category_list")


def course_add(request):

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_course:course_add")
        
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = CourseForm()
    return render(request, "Courses/backend/course-add.html",{'form':form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, "Courses/backend/course-list.html",{'courses':courses})

def course_edit(request, id):
    course = get_object_or_404(Course,id=id)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES,instance=course)

        if form.is_valid():
            form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_course:course_edit")
        
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = CourseForm(instance=course)
    return render(request, "Courses/backend/course-edit.html",{'form':form})

def module_add(request):
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_course:module_add")
        
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = ModuleForm()
    return render(request, "Courses/backend/module-add.html",{'form':form})

def module_list(request):
    modules = Module.objects.all()
    return render(request, "Courses/backend/module-list.html",{'modules':modules})

def module_edit(request,id):
    module = get_object_or_404(Module,id=id)
    if request.method == "POST":
        form = ModuleForm(request.POST,instance=module)
        if form.is_valid():
            form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_course:module_edit")
        
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = ModuleForm(instance=module)
    return render(request, "Courses/backend/module-edit.html",{'form':form})

def resource_add(request):
    if request.method == "POST":
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_course:module_add")
        
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = ResourceForm()
    return render(request, "Courses/backend/resource-add.html",{'form':form})

def resource_list(request):
    resources = Resource.objects.all()
    return render(request, "Courses/backend/resource-list.html",{'resources':resources})

def resource_edit(request, id):
    resource = get_object_or_404(Resource, id=id)
    if request.method == "POST":
        form = ResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_course:module_add")
        
        else:
            messages.error(request, 'Something is wrong!!')
    else:
        form = ResourceForm(instance=resource)
    return render(request, "Courses/backend/resource-add.html",{'form':form})
