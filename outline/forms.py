from django.forms import ModelForm
from outline.models import Profile, Web


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
        fields = '__all__'
