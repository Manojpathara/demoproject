from django import forms


class MyForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=20)
    age = forms.IntegerField()
    department = forms.CharField(max_length=20)
    salary = forms.CharField(max_length=10)
    