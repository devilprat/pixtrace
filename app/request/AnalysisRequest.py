from django import forms


class AnalysisRequest(forms.Form):
    product = forms.IntegerField(required=True)
