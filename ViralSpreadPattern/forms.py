from django import forms

class PatternForm(forms.Form):
    days = forms.IntegerField(required=False)
    probability = forms.DecimalField(required=False)
    inithealth = forms.DecimalField(required=False)