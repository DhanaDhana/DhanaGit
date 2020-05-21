from django import forms
class StudentForm(forms.Form):
    name=forms.CharField(max_length=20)
    marks=forms.IntegerField()
