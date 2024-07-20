from django.contrib import admin

# Register your models here.

from .models import Profile,city

admin.site.register(Profile)
admin.site.register(city)

