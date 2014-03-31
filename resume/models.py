from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Statement(models.Model):
    description = models.CharField(max_length=100)


class Account(models.Model):
    account = models.CharField(max_length=50)
    person = models.ForeignKey(Person)


class Contact(models.Model):
    phone = models.CharField(max_length=15)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    person = models.ForeignKey(Person)


class Skills(models.Model):
    skill_type = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    person = models.ForeignKey(Person)


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
