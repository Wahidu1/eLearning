from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import CommonPage, Testimonial,Contact
from. forms import QueryForm
from django.conf import settings

def about_page(request):
    current_user = request.user

    about = CommonPage.objects.filter(name='about_us').first()
    key_points = about.key_point
    key_point_list = key_points.split(".")

    context = {
        'about':about,
        "key_point_list":key_point_list,
        'current_page':"about",
        'current_user':current_user

        }
    return render(request,"Contents/frontend/about.html",context)

def testimonial_page(request):
    current_user = request.user

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials':testimonials,
        'current_page':"testimonial",
        'current_user':current_user

        }
    return render(request,"Contents/frontend/testmonial.html",context)

def contact_page(request):
    current_user = request.user

    contact = Contact.objects.first()
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            # Save the form data to the Query model
            query_instance = form.save()

            # Extract form data for email
            name = query_instance.name
            email = query_instance.email
            subject = query_instance.subject
            message = query_instance.message
            
            # Compose the email to the admin/recipient
            email_subject = f"New contact form submission: {subject}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            email_from = settings.EMAIL_HOST_USER
            email_to = ['fkwahid00702@gmail.com']  # Replace with the recipient's email address
            
            # Send the email to the admin/recipient
            send_mail(email_subject, email_message, email_from, email_to)

            # Compose the thank you email to the user
            thank_you_subject = "Thank You for Your Feedback!"
            thank_you_message = f"""
            Dear {name},

            Thank you for taking the time to share your feedback with us. We truly appreciate your input and are glad to hear your thoughts on {subject}.

            Your feedback is invaluable to us as we strive to improve and provide the best experience possible.

            If you have any further questions or additional comments, please don't hesitate to reach out to us. We are always here to help.

            Once again, thank you for your feedback.

            Best regards,
            eLearning
            """
            
            # Send the thank you email to the user
            send_mail(thank_you_subject, thank_you_message, email_from, [email])

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('content:contact')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = QueryForm()
    context = {
        'contact':contact,
        'current_page':"contact",
        'form':form,
        'current_user':current_user


        }
    return render(request,"Contents/frontend/contact.html",context)
