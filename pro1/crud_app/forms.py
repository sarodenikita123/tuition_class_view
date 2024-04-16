from django import forms
from .models import Tuition


class TuitionForm(forms.ModelForm):
    class Meta:
        model = Tuition
        fields = "__all__"

        widgets = {
            "student_name ": forms.TextInput(attrs={"class": "form-control"}),
            "previous_marks": forms.TextInput(attrs={"class": "form-control"}),
            "standard": forms.TextInput(attrs={"class": "form-control"}),
            "subject" : forms.TextInput(attrs={"class": "form-control"}),
            "admission_date": forms.TextInput(attrs={"type": "date"}),
        }
