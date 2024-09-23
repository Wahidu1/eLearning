from django.contrib import admin
from .models import Enrollment, Waitlist

admin.site.register(Enrollment)
admin.site.register(Waitlist)

