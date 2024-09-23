from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',include("Home.urls")),
    path('Accounts/',include("Accounts.urls")),
    path('',include("Courses.urls")),
    path('Enrollments/',include("Enrollments.urls")),
    path('Quizzes/',include("Quizzes.urls")),
    path('Progress/',include("Progress.urls")),
    path('Communication/',include("Communication.urls")),
    path('Payments/',include("Payments.urls")),
    path('Analytics/',include("Analytics.urls")),
    path('Contents/',include("Contents.urls")),


    #admin
    path('backend/accounts/',include("Accounts.admin_urls")),
    path('backend/home/',include("Home.admin_urls")),
    path('backend/course/',include("Courses.admin_urls")),
    path('backend/content/',include("Contents.admin_urls")),
    path('backend/communication/',include("Communication.admin_urls")),
    path('backend/enrollments/',include("Enrollments.admin_urls")),





]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
