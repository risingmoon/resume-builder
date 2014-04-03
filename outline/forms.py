from django import forms
from django.forms import ModelForm
from outline.models import Web

class ProfileForm(forms.Form):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'First Name'}))
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'Middle Name'}))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'Last Name'}))
    cell = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'Cell Phone#'}))
    home = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'Home Phone#'}))
    fax = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'Fax Phone#'}))
    address1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'Address1'}))
    address2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'Address2'}))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'City'}))
    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'State'}))
    zipcode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'Zipcode'}))
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'Email'}))
    region = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4 form-control',
                'placeholder': 'region'}))

    # class Meta:
    #     model = Profile
    #     fields = [
    #         'first_name',
    #         'middle_name',
    #         'last_name',
    #         'cell',
    #         'home',
    #         'fax',
    #         'address1',
    #         'address2',
    #         'city',
    #         'state',
    #         'zipcode',
    #         'email',
    #         'region',
    #     ]


class WebForm(ModelForm):
    class Meta:
        model = Web
        fields = ['account']
