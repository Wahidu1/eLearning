from django.urls import path
from . import admin_views

app_name = "backend_enrollment"

urlpatterns = [ 


    path("enrollment-add",admin_views.enrollment_add, name="enrollment_add"),
    path("enrollment-list",admin_views.enrollment_list, name="enrollment_list")


]
