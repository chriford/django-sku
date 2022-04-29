from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("pupils.urls", namespace="pupils")),
    path("", include("teachers.urls", namespace="teachers")),
    path("accounts/", include("authentication.urls", namespace="accounts")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
