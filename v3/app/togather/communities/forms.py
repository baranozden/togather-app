from django import forms
from django.core.exceptions import ValidationError
from .models import Community, CommunityTask


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = "__all__"
        widgets = {
            'users': forms.HiddenInput(),
        }


class CommunityTaskForm(forms.ModelForm):
    class Meta:
        model = CommunityTask
        # fields = "__all__"
        exclude = ("community",)
        widgets = {
            'start_date': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.widgets.DateInput(attrs={'type': 'datetime-local'})
        }