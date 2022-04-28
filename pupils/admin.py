from django.contrib import admin
from .models import Subjects, Question

@admin.register(Subjects)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "subject"
        ,"user"
        ,"question"
        ,"ban_count"
        ,"status"
    )
