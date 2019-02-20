from django.test import TestCase

# Create your tests here.


class TestCatalogo(TestCase):
    def test_smoke(self):
        self.assertEquals(2, 1+1)

    def test_smoke_2(self):
        self.assertFalse(False)
