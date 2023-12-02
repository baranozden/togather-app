from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=256)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        # fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'picture', 'bio', 'country', 'city', 'interest')
        widgets = {
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }