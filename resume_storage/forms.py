from django.forms import Form, BooleanField, ModelForm
from outline.models import Section, Entry, Data
from resume_storage.models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        exclude = ['user', ]


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = '__all__'


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'


class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
