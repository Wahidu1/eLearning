from django.urls import path
from . import admin_views

app_name = "backend_content"
urlpatterns = [
    path('common-page/',admin_views.common_page, name='common_page'),
    path('common-page-edit/<int:id>/',admin_views.common_page_edit, name='common_page_edit'),

    path('contact-page/',admin_views.contact_page, name='contact_page'),
    path('query-list/',admin_views.query_list, name='query_list'),
    path('query-details/<int:id>',admin_views.query_details, name='query_details'),

    path('testimonial-list/',admin_views.testimonial_list, name='testimonial_list'),
    path('testimonial-add/',admin_views.testimonial_add, name='testimonial_add'),
    path('testimonial-edit/<int:id>',admin_views.testimonial_edit, name='testimonial_edit'),








]
