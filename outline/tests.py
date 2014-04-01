from django.test import TestCase
from outline.models import Header, Web, Section, Entry, Data
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            "test",
            "test@example.com",
            "test")
        self.user.save()

    def tearDown(self):
        pass
