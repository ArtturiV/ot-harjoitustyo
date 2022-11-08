import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassan_saldo_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lounaita_myyty_alussa(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)