from django.contrib import admin
from outline.models import Web, Profile, Section, Entry, Data
from resume_storage.models import Resume, Resume_Web, Saved_Section, Saved_Entry


admin.site.register(Web)
admin.site.register(Profile)
admin.site.register(Section)
admin.site.register(Entry)
admin.site.register(Data)
admin.site.register(Resume)
admin.site.register(Saved_Section)
admin.site.register(Saved_Entry)
admin.site.register(Resume_Web)
