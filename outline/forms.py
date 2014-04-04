from django import forms
from django.forms import ModelForm
from outline.models import Profile, Section, Web, Entry, Data

from django.forms.models import BaseInlineFormSet


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'cell',
            'home',
            'fax',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'email',
            'region',
        ]
        widgets = dict()
        for field in fields:
            widgets[field] = forms.TextInput(attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': ' '.join(
                    [f.capitalize() for f in field.split('_')]
                )}
            )


class WebForm(ModelForm):
    class Meta:
        model = Web
        fields = ['account']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = [
            'title',
            'description',
        ]


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [
            'title',
            'subtitle',
            'start_date',
            'end_date',
            'present',
            'city',
            'state',
            'contact',
            'description',
            'display',
        ]


class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = [
            'text'
        ]

