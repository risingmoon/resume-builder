from django.test import TestCase
from outline.models import Photo, Album, Tag
from django.contrib.auth.models import User

# Create your tests here.


class BasicTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            "test",
            "test@example.com",
            "test")
        self.user.save()


# class HeaderTest(self):

#     def test_