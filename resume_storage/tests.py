from django.test import TestCase
from outline.models import Section, Entry, Data
from models import Resume, Resume_Web, Saved_Section, Saved_Entry
from django.contrib.auth.models import User


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
                    Data.objects.create(text=atext)

    def testGetResume(self):
        newResume = Resume.objects.create(first_name='jack',
                                          last_name='markley',
                                          user=self.testUser)
        self.assertEqual(newResume.getResumeFields(), (newResume, {}))
        
        newResume = Resume.objects.create(first_name='mark',
                                          last_name='charyk',
                                          user=self.testUser)
        

    def testSetResume(self):
        pass
