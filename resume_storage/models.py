from django.db import models
from outline.models import Section, Entry, Data
from django.contrib.auth.models import User


class Resume_Web(models.Model):
    account = models.CharField(max_length=50)


class Resume(models.Model):
    #metadatas
    title = models.CharField(max_length=64)
    user = models.ForeignKey(User)

    #header fields
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    cell = models.CharField(max_length=15, null=True)
    home = models.CharField(max_length=15, null=True)
    fax = models.CharField(max_length=15, null=True)
    address1 = models.CharField(max_length=50, null=True)
    address2 = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    web = models.ManyToManyField(Resume_Web, null=True)

    def setResumeFields(self):
        pass

    def getResumeFields(self):
        secEntDats = {}
        for eachSection in Saved_Section.objects.filter(resume=self):
            EntDats = {}
            for eachEntry in Saved_Entry.objects.filter(section=eachSection):
                Dats = []
                for eachData in Data.objects.filter(entry=eachEntry):
                    Dats.append(eachData)
                EntDats[eachEntry] = Dats
            secEntDats[eachSection] = EntDats
        return self, secEntDats


class Saved_Section(models.Model):
    resume = models.ForeignKey(Resume)
    section = models.ForeignKey(Section)


class Saved_Entry(models.Model):
    section = models.ForeignKey(Saved_Section)
    entry = models.ForeignKey(Entry)
    dataset = models.ManyToManyField(Data)
