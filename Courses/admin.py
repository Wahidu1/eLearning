from django.contrib import admin
from .models import Course, Module, Resource,Category

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Resource)

