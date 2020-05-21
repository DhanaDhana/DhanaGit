from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(max_length=50)
    salary=forms.IntegerField()
    email=forms.EmailField(max_length=50)
    location=forms.CharField(max_length=50)
