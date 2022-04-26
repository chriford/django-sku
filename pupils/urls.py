from django.urls import path
from .views import QuestionListView

urlpatterns = [
    path("question/list/", QuestionListView.as_view(), name="questions")
]