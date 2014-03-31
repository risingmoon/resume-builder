from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Web(models.Model):
    account = models.CharField(max_length=50)


class Header(models.Model):
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
    web = models.ManyToManyField(Web, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(' '.join[
            self.first_name,
            self.middle_name,
            self.last_name])

    def middle_intial(self):
        return unicode(' '.join[
            self.first_name,
            self.middle_name[0] + '.',
            self.last_name])


class Section(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.title)


class Entry(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    section = models.ForeignKey('Section')

    def __unicode__(self):
        return unicode(self.title)

    def yield_date(self):
        if self.start_date and self.end_date:
            return unicode(" - ".join([
                self.start_date,
                self.end_date]))


class Data(models.Model):
    text = models.CharField(max_length=400)
    entry = models.ForeignKey('Entry')
