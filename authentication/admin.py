from django.contrib import admin
from .models import User

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
# Register your models here.
