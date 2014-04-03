from django.forms import ModelForm
# from django.forms.models import inlineformset_factory
from outline.models import Profile, Web, Section, Data


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


class WebForm(ModelForm):
    class Meta:
        model = Web
        fields = ['account']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        field = [
            'title',
            'description',
        ]


class EntryForm(ModelForm):
    class Meta:
        model = Section
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
        field = [
            'text'
        ]
