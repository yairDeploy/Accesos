from django.test import TestCase
from vehiculos.views import Vehiculos
# Create your tests here.


class TestCatalogo(TestCase):
    def test_smoke(self):
        self.assertEquals(2, 1+1)

    def test_smoke_2(self):
        self.assertFalse(False)

    def test_view_true(self):
        self.assertTrue(Vehiculos.altavehiculos(True))

    def test_view_false(self):
        self.assertFalse(Vehiculos.altavehiculos(False))
