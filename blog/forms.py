from django import forms

from blog.models import Contact


class ContactusForm(forms.Form):
    fullname = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=250)
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)
