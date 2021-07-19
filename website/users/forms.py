# users/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CountryForm(forms.Form):
    country_name = forms.CharField(label='countryName', max_length=40)
