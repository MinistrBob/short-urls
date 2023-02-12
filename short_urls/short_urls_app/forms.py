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


class AddLinkForm(forms.Form):
    short_url = forms.SlugField(max_length=80,
                                label="Короткая ссылка",
                                widget=forms.TextInput(attrs={'class': 'form-input'}))
    is_enabled = forms.BooleanField(label="Включено?",
                                    help_text='Программа делает перенаправление только для включенных ссылок',
                                    required=False,
                                    initial=True)
    long_url = forms.CharField(max_length=65535,
                               widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),
                               label="Длинная ссылка")
