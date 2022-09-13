from dataclasses import fields
from django.forms import ModelForm
from .models import Contact, UrunForm
from django import forms

from django.contrib.auth.models import User
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control float-start mb-4 is-invalid', 'placeholder': 'İsim', 'id': 'name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control float-end mb-4 is-invalid', 'placeholder': 'E-mail', 'id': 'email'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control mb-4 is-invalid', 'placeholder': 'Subject', 'id': 'subject'})
        self.fields['message'].widget.attrs.update({'class': 'form-control text-black-50 mb-4 is-invalid', 'placeholder': 'Mesajınızı Yazınız', 'id': 'message'})


class CreateForm(ModelForm):
    class Meta:
        model = UrunForm
        fields = [ 'resim', 'fiyat', 'aciklama']

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3'})