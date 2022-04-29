from django.forms import ModelForm, widgets
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import (
    Layout,
    HTML,
    Fieldset,
    Submit,
    Row,
    Column,
)

from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ["slug", "ban_count", "status"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column("user", css_class="form-group col-md-12 mb-0"),
                Column("subject", css_class="form-group col-lg-12"),
                Column("question", css_class="form-control col-md-12 mb-0"),
            )
        )

    def save(self, commit=True):
        instance = super(QuestionForm, self).save(commit=False)
        instance.save()
        return instance
