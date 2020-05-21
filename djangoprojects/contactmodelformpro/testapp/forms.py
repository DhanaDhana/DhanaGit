from django import forms
from testapp.models import ContactData
class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactData
        fields='__all__'
