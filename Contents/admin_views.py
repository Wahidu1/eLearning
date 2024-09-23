from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import CommonPage, Contact, Query, Testimonial
from .admin_forms import CommonPageForm, ContactForm, TestimonialForm
from django.contrib import messages

def common_page(request):
    common_page_contents = CommonPage.objects.all()
    return render(request, 'Contents/backend/common-page-list.html',{'common_page_contents':common_page_contents})

def common_page_edit(request,id):
    common_page_content = get_object_or_404(CommonPage, id=id)

    if request.method == "POST":
        form = CommonPageForm(request.POST, request.FILES, instance=common_page_content)

        if form.is_valid():
            form.save()
            messages.success(request, 'Save Successfully')
            return redirect("backend_content:common_page_edit", id=id)
        else: 
            
            messages.error(request, 'Update Failed')
        
    else:
        form = CommonPageForm(instance=common_page_content)

    return render(request, 'Contents/backend/common-page-edit.html',{"form":form})

def contact_page(request):
    contact = Contact.objects.all().first()
    if request.method == "POST":
        form = ContactForm(request.POST, instance= contact)

        if form.is_valid():
            form.save()
            messages.success(request, "Update Successfully")
            return redirect("backend_content:contact_page")
        else:
            messages.error(request, "Update Failed")
    else:
        form = ContactForm(instance=contact)
    return render(request, "Contents/backend/contact-page.html",{'form':form})

def query_list(request):
    queries = Query.objects.all()
    return render(request, "Contents/backend/query-list.html",{"queries" : queries})

def query_details(request, id):
    query = get_object_or_404(Query, id=id)
    return render(request, "Contents/backend/query-details.html",{"query" : query})

def testimonial_add(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect("backend_content:testimonial_add")
        else:
            messages.error(request, "Failed")
    else:
        form = TestimonialForm()
    return render(request, "Contents/backend/testimonial-add.html",{"form" : form})

def testimonial_edit(request,id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect("backend_content:testimonial_edit", id =id)
        else:
            messages.error(request, "Failed")
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, "Contents/backend/testimonial-edit.html",{"form" : form})
def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, "Contents/backend/testimonial-list.html",{"testimonials" : testimonials})


