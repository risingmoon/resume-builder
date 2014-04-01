from django.test import TestCase
from outline.models import Header, Section, Web, Entry, Data
from django.contrib.auth.models import User
from datetime import date

# Create your tests here.


class BasicTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            "John",
            "johndoe@gmail.com",
            "password")
        self.user.save()

        w1 = Web(text="http://www.twitter.com")
        w2 = Web(text="http://www.github.com")
        w3 = Web(text="http://www.linkedIn.com")

        header = Header(
            first_name="John",
            middle_name="Fake",
            last_name="Doe",
            cell="(123)456-7890",
            home="(234)567-8901",
            fax="(345)678-9012",
            address1="1234 Spoon St.",
            address2="APT 5",
            city="Seattle",
            State="WA",
            zipcode="98021",
            email="johndoe@gmail.com",
            region="Great Seattle Area",
            user=self.user)

        header.add([w1, w2, w3])

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

        college = Entry(
            title="Bachelor of Science in Pythonic Interpretation",
            start_date=date(2007, 9, 1),
            end_date=date(20011, 5, 1),
            city="Baltimore",
            state="MD",
            section=education)
        college.save()

        work = Entry(
            title="Code Fellows",
            subtitle="Python Newbie",
            start_date=date(2007, 9, 1),
            end_date=date(20011, 5, 1),
            city="Baltimore",
            state="MD",
            section=education)
        work.save()

        d1 = Data(
            text="Built Flask Microblog",
            entry=work)
        d1.save()

        d2 = Data(
            text="Built Haikute",
            entry=work)
        d2.save()

        d3 = Data(
            text="Built Django Sharing App",
            entry=work)
        d3.save()


class HeaderTest(BasicTest):

    def test_something(self):
        pass
