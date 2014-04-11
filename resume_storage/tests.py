from django.test import TestCase
from outline.models import Section, Entry, Data
from models import Resume, Saved_Section, Saved_Entry
from django.contrib.auth.models import User
from django.test import Client
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden, HttpResponseNotFound


class ResumeStorageTestCase(TestCase):

    def setUp(self):
        self.testUser = User.objects.create_user('testperson',
                                                 'fake@email.ro',
                                                 'badpass',)
        Resume.objects.create(first_name='test',
                              last_name='user',
                              user=self.testUser)
        for atitle in ('one title', 'two title', 'red title', 'blue title'):
            asection = Section.objects.create(title=atitle, user=self.testUser)
            for anothertitle in ('big title', 'small title', 'sub title'):
                anentry = Entry.objects.create(title=anothertitle,
                                               section=asection,)
                for atext in ('almost', 'done'):
                    Data.objects.create(text=atext, entry=anentry)

    def testGetResume(self):
        newResume = Resume.objects.create(first_name='jack',
                                          last_name='markley',
                                          user=self.testUser)
        self.assertEqual(newResume.getResumeFields(), {})

        newResume = Resume.objects.create(first_name='mark',
                                          last_name='charyk',
                                          user=self.testUser)
        sectdict = {}
        for atitle in ('a', 'no', 'the', 'why'):
            asection = Section.objects.create(title=atitle, user=self.testUser)
            sectdict[asection] = {}
            for anothertitle in ('top', 'bot', 'mid'):
                anentry = Entry.objects.create(title=anothertitle,
                                               section=asection,)
                sectdict[asection][anentry] = []
                for atext in ('makeit', 'end'):
                    newdata = Data.objects.create(text=atext, entry=anentry)
                    sectdict[asection][anentry].append(newdata)
        result = newResume.getResumeFields()
        for savesect in result.keys():
            assert savesect.section in sectdict.keys()

    def testSetResume(self):
        newResume = Resume.objects.create(first_name='jack',
                                          last_name='markley',
                                          user=self.testUser)
        Section.objects.create(user=self.testUser, title='invissection')
        mysection = Section.objects.create(user=self.testUser,
                                           title='vissection')
        Entry.objects.create(section=mysection, title='invisentry')
        myentry = Entry.objects.create(section=mysection,
                                       title='visentry')
        Data.objects.create(entry=myentry, text='invisdata')
        mydata = Data.objects.create(entry=myentry,
                                     text='visdata')
        fieldDict = {mysection: {myentry: [mydata]}}

        newResume.setResumeFields(fieldDict)
        for eachSection in Saved_Section.objects.filter(resume=newResume):
            assert eachSection.section in fieldDict.keys()
            for eachEntry in Saved_Entry.objects.filter(section=eachSection):
                assert eachEntry.entry in fieldDict[eachSection.section].keys()


class TestViews(TestCase):
    fixtures = ['test_fixture.json', ]

    def setUp(self):
        self.client = Client()
        self.client.login(username='admin', password='admin')

    def tearDown(self):
        self.client.logout()

    def test_front_logged_out(self):
        self.client.logout()
        resp = self.client.get(reverse('index'))
        self.assertContains(resp, 'Resume Storage Front page')

    def test_front_logged_in(self):
        resp = self.client.get(reverse('index'), follow=True)
        self.assertContains(resp, 'Print this resume')

    def test_home_logged_out(self):
        self.client.logout()
        resp = self.client.get(reverse('home'), follow=True)
        self.assertContains(resp, 'Please log in')

    def test_home_logged_in(self):
        resp = self.client.get(reverse('home'))
        self.assertContains(resp, 'Print this resume')

    def test_create(self):
        resp = self.client.get(reverse('create_resume'), follow=True)
        self.assertContains(resp, 'Edit Resume')
        Resume.objects.get(pk=43)

    def test_resume_view(self):
        resp = self.client.get(reverse('resume_view', args=(40,)), follow=True)
        self.assertContains(resp, 'New Resume')
        self.assertContains(resp, 'Joseph')

    def test_other_users_resume(self):
        resp = self.client.get(reverse('resume_view', args=(36,)), follow=True)
        self.assertIsInstance(resp, HttpResponseForbidden)

    def test_no_resume(self):
        resp = self.client.get(reverse('resume_view', args=(45,)), follow=True)
        self.assertIsInstance(resp, HttpResponseNotFound)

    def test_resume_post_sparse(self):
        self.client.post(reverse('resume_view', args=(40,)), {
            'First Name': True,
            'Last Name': True,
            'title': 'NewER Resume',
            })
        resum = Resume.objects.get(pk=40)
        self.assertEqual(resum.title, 'NewER Resume')
        self.assertEqual(resum.cell, '')
        self.assertEqual(resum.fax, '')
        self.assertEqual(resum.first_name, 'Mark')
        self.assertEqual(resum.last_name, 'Charyk')

    def test_resume_post_surfeit(self):
        self.client.post(reverse('resume_view', args=(40,)), {
            'title': 'New Resume',
            'First Name': True,
            'Last Name': True,
            'Middle name': True,
            'Cell': True,
            'Home': True,
            'Address1': True,
            'Address2': True,
            'City': True,
            'State': True,
            'Zipcode': True,
            'Email': True,
            'Region': True,
            })
        resum = Resume.objects.get(pk=40)
        self.assertEqual(resum.title, 'New Resume')
        self.assertEqual(resum.cell, '(555) 555-6577')
        self.assertEqual(resum.middle_name, 'Joseph')
        self.assertEqual(resum.city, 'Seattle')
        self.assertEqual(resum.fax, '')
