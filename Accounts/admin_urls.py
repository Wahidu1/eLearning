from django.urls import path
from . import admin_views

app_name = "backend_account"

urlpatterns = [ 

    # Admin
    path('login/',admin_views.backend_login,name="backend_login"),
    path('instructor-add/',admin_views.backend_instructor_add,name="backend_instructor_add"),
    path('instructor-list/',admin_views.backend_instructor_list,name="backend_instructor_list"),
    path('instructor-edit/<int:id>/',admin_views.backend_instructor_edit,name="backend_instructor_edit"), 
    path('instructor-delete/<int:id>/',admin_views.backend_instructor_delete,name="backend_instructor_delete"), 


    path('student-add/',admin_views.backend_student_add,name="backend_student_add"),
    path('student-list/',admin_views.backend_student_list,name="backend_student_list"),
    path('student-edit/<int:id>/',admin_views.backend_student_edit,name="backend_student_edit"), 
    path('student-delete/<int:id>/',admin_views.backend_student_delete,name="backend_student_delete"),
    path('get-student-info/<int:roll_number>/', admin_views.get_student_info, name='get_student_info'),




]