from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Web(models.Model):
    account = models.CharField(max_length=50)


class Header(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cell = models.CharField(max_length=15)
    home = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    web = models.ManyToManyField(Web)
    user = models.ForeignKey(User)


class Section(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    user = models.ForeignKey(User)


class Entry(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    section = models.ForeignKey('Section')


class Data(models.Model):
    text = models.CharField(max_length=400)

class Education(models.Model):
    certificate = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    #Change
    date = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    person = models.ForeignKey(Person)


class Experience(models.Model):
    employer = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    person = models.ForeignKey(Person)


class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    person = models.ForeignKey(Person)


class Activities(models.Model):
    description = models.CharField(max_length=50)
    person = models.ForeignKey(Person)


class Interests(models.Model):
    description = models.CharField(max_length=50)
    person = models.ForeignKey(Person)
