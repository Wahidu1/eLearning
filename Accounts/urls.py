from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('our-team/',views.our_team_page,name="our_team"),
    path('student-add/',views.student_add,name="student_add"),
    path('login/',views.login_page,name="login"),
    path('profile/',views.profile_page,name="profile"),

]
