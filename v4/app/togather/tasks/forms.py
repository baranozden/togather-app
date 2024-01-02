from django import forms
from django.core.exceptions import ValidationError
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = "__all__"
        exclude = ("user",)
        widgets = {
            'start_date': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.widgets.DateInput(attrs={'type': 'datetime-local'})
        }

    def clean(self):
        start_date = self.cleaned_data["start_date"]
        end_date = self.cleaned_data["end_date"]
        if end_date <= start_date:
            raise ValidationError("End date should be later than start date.")
        return self.cleaned_data