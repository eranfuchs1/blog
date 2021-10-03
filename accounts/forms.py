from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'password confirm'
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
