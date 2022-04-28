from django.urls import path
from .views import AnswerListView

app_name = "teachers"
urlpatterns = [
    path("answers/list/", AnswerListView.as_view(), name="answers")
]
