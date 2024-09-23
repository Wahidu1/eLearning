from django.urls import path
from . import admin_views

app_name ='backend_home'
urlpatterns = [
    path('dashboard/',admin_views.backend_dashboard,name="backend_dashboard"),
]