from django.test import TestCase
from outline.models import Profile, Section, Web, Entry, Data
from django.contrib.auth.models import User
from datetime import date
import pdb

# Create your tests here.


class BasicTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            "John",
            "johndoe@gmail.com",
            "password")
        self.user.save()

        w1 = Web.objects.create(account="http://www.twitter.com")
        w1.save()
        w2 = Web.objects.create(account="http://www.github.com")
        w2.save()
        w3 = Web.objects.create(account="http://www.linkedIn.com")
        w3.save()

        self.profile = Profile.objects.create(
            first_name="John",
            middle_name="Fake",
            last_name="Doe",
            cell="(123)456-7890",
            home="(234)567-8901",
            fax="(345)678-9012",
            address1="1234 Spoon St.",
            address2="APT 5",
            city="Seattle",
            state="WA",
            zipcode="98021",
            email="johndoe@gmail.com",
            region="Great Seattle Area",
            user=self.user)
        self.profile.webs = [w1, w2, w3]
        self.profile.save()

        objective = Section(
            title="objective",
            description="I want a job",
            user=self.user)
        objective.save()

        education = Section(
            title="education",
            user=self.user)
        education.save()

        experience = Section(
            title="experience",
            user=self.user)
        experience.save()

        # pdb.set_trace()

        self.college = Entry(
            title="Bachelor of Science in Pythonic Interpretation",
            start_date=date(2007, 9, 1),
            end_date=date(2011, 5, 1),
            city="Baltimore",
            state="MD",
            section=education)
        self.college.save()

        self.work = Entry(
            title="Code Fellows",
            subtitle="Python Newbie",
            start_date=date(2014, 2, 1),
            present=True,
            city="Baltimore",
            state="MD",
            section=education)
        self.work.save()

        d1 = Data(
            text="Built Flask Microblog",
            entry=self.work)
        d1.save()

        d2 = Data(
            text="Built Haikute",
            entry=self.work)
        d2.save()

        d3 = Data(
            text="Built Django Sharing App",
            entry=self.work)
        d3.save()


class HeaderTest(BasicTest):

    def test_middle_initial(self):
        self.assertEqual(
            "John F. Doe", self.profile.middle_initial())

    def test_no_middle_initial(self):
        user = User.objects.create_user(
            "Jane",
            "janedoe@gmail.com",
            "password")
        user.save()
        profile = Profile.objects.create(
            first_name="Jane",
            last_name="Doe",
            user=user)
        profile.save()
        self.assertEqual(
            "Jane Doe", profile.middle_initial())
    
    def test_long_month(self):
        self.assertEqual(
            self.college.date_string(0),
            "September 2007-May 2011")
        self.assertEqual(
            self.work.date_string(0),
            "February 2014-Present")

    def test_short_month(self):
        self.assertEqual(
            self.college.date_string(1),
            "Sep 2007-May 2011")
        self.assertEqual(
            self.work.date_string(1),
            "Feb 2014-Present")

    def test_standard_date(self):
        self.assertEqual(
            self.college.date_string(2),
            "9/1/07-5/1/11")
        self.assertEqual(
            self.work.date_string(2),
            "2/1/14-Present")





