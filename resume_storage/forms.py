from django.forms import BooleanField, ModelForm
from outline.models import Section, Entry, Data
from resume_storage.models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        exclude = ['user', ]

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        readonlies = self.fields.copy()
        order = ['title']
        for item in readonlies:
            if item != 'title':
                self.fields[item].widget.attrs['readonly'] = True
                self.fields["Include %s?" % item] = BooleanField(
                    required=False,
                    initial=True
                )
                order.extend([item, "Include %s?" % item])
        self.fields.keyOrder = order


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
