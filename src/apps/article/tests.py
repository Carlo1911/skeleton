from django.test import TestCase
from article.models import Reporter

class ReporterTestCase(TestCase):
    def setUp(self):
        Reporter.objects.create(name='Manuel')

    def test_reporters(self):
        manuel = Reporter.objects.get(name="Manuel")
        self.assertEqual(manuel.name, 'Manuel')