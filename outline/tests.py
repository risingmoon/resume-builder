from django.test import TestCase
from outline.models import Header
from django.contrib.auth.models import User

# Create your tests here.


class BasicTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            "John",
            "johndoe@gmail.com",
            "password")
        self.user.save()

        w1 = Web(text="http://www.twitter.com/twitter")
        w2 = Web(text="http://www.ithub.com/github")
        w3 = Web(text="http://www.linkedIn/in/Linkedin")

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
            )

        header.add = [w1, w2, w3]
        


# class HeaderTest(self):

#     def test_