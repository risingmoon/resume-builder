from django.db import models
from django.contrib.auth.models import User
import pdb
# Create your models here.


class Web(models.Model):
    account = models.CharField(max_length=50)

    def __unicode__(self):
        return self.account


class Profile(models.Model):
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
    webs = models.ManyToManyField(Web, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        if self.middle_name:
            return unicode(' '.join([
                self.first_name,
                self.middle_name,
                self.last_name]))
        else:
            return unicode(' '.join([
                self.first_name,
                self.last_name]))
        
    def middle_initial(self):
        "Returns full name with middle initial"
        if self.middle_name:
            # pdb.set_trace()
            return unicode(' '.join([
                self.first_name,
                self.middle_name[0] + '.',
                self.last_name]))
        else:
            return unicode(' '.join([
                self.first_name,
                self.last_name]))

    def city_state_zip(self):
        if self.city and self.state and self.zipcode:
            return self.city + "," + self.state + " " + self.zipcode


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
    present = models.NullBooleanField(null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    section = models.ForeignKey('Section')

    def __unicode__(self):
        return unicode(self.title)

    def date_string(self, num):
        format = {0: "%B %Y", 1: "%b %Y", 2: "%x"}
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
