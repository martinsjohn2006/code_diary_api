"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from models_app import models
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    """Defining the admin pages for the users"""
    

