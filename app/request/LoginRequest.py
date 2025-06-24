from django import forms


class LoginRequest(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(min_length=8, required=True)
