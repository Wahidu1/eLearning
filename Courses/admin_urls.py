from django.urls import path
from . import admin_views
app_name = "backend_course"
urlpatterns = [

    #Course Category
    path('course-category-add/',admin_views.course_category_add,name="course_category_add"),
    path('course-category-list/',admin_views.course_category_list,name="course_category_list"),
    path('course-category-edit/<int:id>',admin_views.course_category_edit,name="course_category_edit"),
    path('course-category-delete/<int:id>',admin_views.course_category_delete,name="course_category_delete"),

    path('course-add/',admin_views.course_add,name="course_add"),
    path('course-list/',admin_views.course_list,name="course_list"), 
    path('course-edit/<int:id>',admin_views.course_edit,name="course_edit"),
    # path('course-delete/<int:id>',admin_views.course_delete,name="course_delete"),


    path('module-add/',admin_views.module_add,name="module_add"),
    path('module-list/',admin_views.module_list,name="module_list"),
    path('module-edit/<int:id>',admin_views.module_edit,name="module_edit"),

    path('resource-add/',admin_views.resource_add,name="resource_add"),
    path('resource-list/',admin_views.resource_list,name="resource_list"),
    path('resource-edit/<int:id>',admin_views.resource_edit,name="resource_edit"),


















]
