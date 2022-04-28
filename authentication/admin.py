from django.contrib import admin
from .models import User, UserProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "username",
        "email",
        "created"
    ]
    list_filter = [
        "created",
    ]
    list_per_page = 12
    
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user"
        ,"grade"
        ,"sex"
        ,"about_me"
        ,"cell"
    ]