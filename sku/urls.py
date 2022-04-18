from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("code_shine.urls")),
    path('admin/', admin.site.urls),
]
