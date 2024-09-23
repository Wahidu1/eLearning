from django.urls import path
from . import views

app_name = "course"
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('course-category-details/<int:id>/',views.course_category_details,name='course_category_details'),
    path('course-details/<int:id>/',views.course_details,name='course_details'),
    path('course/',views.course_page,name='course'),
    path('my_course/',views.my_course_page,name='my_course'),
    path('my_course/<int:id>/',views.course_module,name='course_module'),





]
