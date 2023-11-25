from django import forms
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