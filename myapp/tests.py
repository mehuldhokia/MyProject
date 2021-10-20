from django.test import TestCase
from myapp.models import Student

# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(sname="Krishna", course="BCA", sem="3")
        Student.objects.create(sname="Sudama", course="BCA", sem="4")

    def test_students_can_display(self):
        """Students information are correctly identified"""
        krishna = Student.objects.get(sname="Krishna")
        sudama  = Student.objects.get(sname="Sudama")
        # self.assertEqual(krishna.display(), 'The krishna is in BCA Sem-3')
        # self.assertEqual(sudama.display() , 'The Sudama is in BCA Sem-4')
        self.assertEqual(krishna.display(), 'Roll 1 : Student Krishna, Course BCA - Sem 3')
        self.assertEqual(sudama.display() , 'Roll 2 : Student Sudama, Course BCA - Sem 4')