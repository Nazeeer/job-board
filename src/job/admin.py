from django.contrib import admin

# Register your models here.

from .models import Job,category,apply

admin.site.register(Job)
admin.site.register(category)
admin.site.register(apply)
