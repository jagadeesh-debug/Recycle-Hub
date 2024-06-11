# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Custom_User, Map

# Register the custom user model and the custom admin class
admin.site.register(Map)
