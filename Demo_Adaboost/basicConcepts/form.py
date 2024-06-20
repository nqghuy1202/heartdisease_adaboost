from django import forms

class TestForm(forms.Form):
    age = forms.CharField(max_length=10)
