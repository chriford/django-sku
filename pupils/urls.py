from django.urls import path
from .views import QuestionListView, UserQuestionListView

app_name = "pupils"
urlpatterns = [
    path("question/list/", QuestionListView.as_view(), name="questions"),
    path("user/question/list/", UserQuestionListView.as_view(), name="user-questions"),
]