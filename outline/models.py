from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Web(models.Model):
    account = models.CharField(max_length=50)


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    cell = models.CharField(max_length=15, blank=True)
    home = models.CharField(max_length=15, blank=True)
    fax = models.CharField(max_length=15, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    web = models.ManyToManyField(Web, blank=True)
    user = models.ForeignKey(User)

    # def __unicode__(self):
    #     return unicode(' '.join[
    #         self.first_name,
    #         self.middle_name,
    #         self.last_name])

    # def middle_initial(self):
    #     return unicode(' '.join[
    #         self.first_name,
    #         self.middle_name[0] + '.',
    #         self.last_name])


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

    def yield_date(self, num):
        if self.start_date and self.end_date:
            dat_str = [
                self.start_date.strftime(format[num]),
                self.end_date.strftime(format[num])]
            return "-".join(dat_str)
        elif self.start_date and self.present:
            dat_str = [
                self.start_date.strftime(format[num]),
                "Present"]
            return "-".join(dat_str)


class Data(models.Model):
    text = models.CharField(max_length=400)
    entry = models.ForeignKey('Entry')
