from django.urls import path
from . import views

app_name = "content"
urlpatterns = [
    path('about/',views.about_page,name='about'),
    path('testimonial/',views.testimonial_page,name='testimonial'),
    path('contact/',views.contact_page,name='contact'),


]
