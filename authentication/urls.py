from django.urls import path
from . import views

app_name = "authentication"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.register, name="register"),
    path("users/", views.SystemUsersListView.as_view(), name="users"),
    path("", views.HomeListView.as_view(), name="home"),
]
