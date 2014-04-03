from django.forms import ModelForm
# from django.forms.models import inlineformset_factory
from outline.models import Profile, Web, Section


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


class Section(ModelForm):
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
            'descriptio',
            'section',
            'display',
        ]