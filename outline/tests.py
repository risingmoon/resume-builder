from django.test import TestCase
from outline.models import Profile, Section, Web, Entry, Data
from django.contrib.auth.models import User
from datetime import date


class BasicTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            "John",
            "johndoe@gmail.com",
            "password")
        self.user.save()

        w1 = Web.objects.create(account="http://www.twitter.com")
        w2 = Web.objects.create(account="http://www.github.com")
        w3 = Web.objects.create(account="http://www.linkedIn.com")

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

        self.profile.web = [w1, w2, w3]

        objective = Section.objects.create(
            title="objective",
            description="I want a job",
            user=self.user)
        objective.save()

        self.education = Section.objects.create(
            title="education",
            user=self.user)
        self.education.save()

        self.experience = Section.objects.create(
            title="experience",
            user=self.user)
        self.experience.save()

        self.skills = Section.objects.create(
            title="Skill",
            user=self.user)
        self.skills.save()

        self.college = Entry.objects.create(
            title="Bachelor of Science in Pythonic Interpretation",
            start_date=date(2007, 9, 1),
            end_date=date(2011, 5, 1),
            city="Baltimore",
            state="MD",
            section=self.education)
        self.college.save()

        self.programming = Entry.objects.create(
            title="Programming",
            section=self.skills)
        self.programming.save()

        self.work = Entry.objects.create(
            title="Code Fellows",
            subtitle="Python Newbie",
            start_date=date(2014, 2, 1),
            present=True,
            city="Baltimore",
            state="MD",
            section=self.experience,
            display="L")
        self.work.save()

        

        d1 = Data.objects.create(
            text="Built Flask Microblog",
            entry=self.work)
        d1.save()

        d2 = Data.objects.create(
            text="Built Haikute",
            entry=self.work)
        d2.save()

        d3 = Data.objects.create(
            text="Built Django Sharing App",
            entry=self.work)
        d3.save()

        d4 = Data.objects.create(
            text="Django",
            entry=self.programming)
        d4.save()

        d5 = Data.objects.create(
            text="Python",
            entry=self.programming)
        d5.save()

        d6 = Data.objects.create(
            text="Java",
            entry=self.programming)
        d6.save()

        d7 = Data.objects.create(
            text="iOS",
            entry=self.programming)
        d7.save()


class HeaderTest(BasicTest):

    # def test_middle_initial(self):
    #     self.assertEqual(
    #         "John F. Doe", self.profile.middle_initial())

    # def test_no_middle_initial(self):
    #     user = User.objects.create_user(
    #         "Jane",
    #         "janedoe@gmail.com",
    #         "password")
    #     user.save()
    #     profile = Profile.objects.create(
    #         first_name="Jane",
    #         last_name="Doe",
    #         user=user)
    #     profile.save()
    #     self.assertEqual(
    #         "Jane Doe", profile.middle_initial())

    # def test_long_month(self):
    #     self.assertEqual(
    #         self.college.date_string(0),
    #         "September 2007-May 2011")
    #     self.assertEqual(
    #         self.work.date_string(0),
    #         "February 2014-Present")

    # def test_short_month(self):
    #     self.assertEqual(
    #         self.college.date_string(1),
    #         "Sep 2007-May 2011")
    #     self.assertEqual(
    #         self.work.date_string(1),
    #         "Feb 2014-Present")

    # def test_standard_date(self):
    #     self.assertEqual(
    #         self.college.date_string(2),
    #         "09/01/07-05/01/11")
    #     self.assertEqual(
    #         self.work.date_string(2),
    #         "02/01/14-Present")

    # def test_city_state_zip(self):
    #     self.assertEqual(
    #         self.profile.city_state_zip(),
    #         "Seattle, WA 98021")

    def test_delimited(self):
        self.assertEqual(
            "iOS, Java, Python, Django",
            self.programming.delimited())
    
    def test_listed(self):
        self.assertEqual(
            """-Built Django Sharing App
-Built Haikute\n-Built Flask Microblog""",
            self.work.listed('-'))


