from django.contrib import admin
from outline.models import Web, Header, Section, Entry, Data
from resume_storage.models import Resume, Saved_Section, Saved_Entry


admin.site.register(Web)
admin.site.register(Header)
admin.site.register(Section)
admin.site.register(Entry)
admin.site.register(Data)
admin.site.register(Resume)
admin.site.register(Saved_Section)
admin.site.register(Saved_Entry)
