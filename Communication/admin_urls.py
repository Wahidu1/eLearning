from django.urls import path
from . import admin_views

app_name = "backend_communication"

urlpatterns = [ 


    path("notification-add",admin_views.notification_add, name="notification_add"),
    path("notification-list",admin_views.notification_list, name="notification_list")


]