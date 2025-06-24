from django import forms


class SearchRequest(forms.Form):
    file = forms.FileField(required=True)
