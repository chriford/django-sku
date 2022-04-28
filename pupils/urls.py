from django.urls import path
from .views import QuestionListView

app_name = "pupils"
urlpatterns = [
    path("question/list/", QuestionListView.as_view(), name="questions")
]