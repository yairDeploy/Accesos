from django.test import TestCase

# Create your tests here.
class TestCatalogo(TestCase):
    def test_smoke(self):
        self.assertEquals(2,1+1)