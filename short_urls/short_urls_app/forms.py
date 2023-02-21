from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class AuthForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"


class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['short_url', 'is_enabled', 'long_url']
        widgets = {
            'short_url': forms.TextInput(attrs={'class': 'form-input'}),
            'long_url': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"


class EditLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
