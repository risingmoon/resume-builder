from django.db import models
from outline.models import Header, Section, Entry, Data
from django.contrib.auth.models import User


# def get_user():
#     return User.objects.get(pk=1)


class Resume(models.Model):
    title = models.CharField(max_length=64)
    header = models.OneToOneField(Header)
    user = models.ForeignKey(User)


class Saved_Section(models.Model):
    resume = models.ForeignKey(Resume)
    section = models.ForeignKey(Section)


class Saved_Entry(models.Model):
    section = models.ForeignKey(Saved_Section)
    entry = models.ForeignKey(Entry)
    dataset = models.ManyToManyField(Data)
