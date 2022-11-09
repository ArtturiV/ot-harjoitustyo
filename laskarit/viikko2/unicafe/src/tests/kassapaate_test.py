import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassan_saldo_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lounaita_myyty_alussa(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_maukas_kateisosto_lisaa_kassaan_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullinen_kateisosto_lisaa_kassaan_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukas_kateisosto_antaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_edullinen_kateisosto_antaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_maukas_kateisosto_lisaa_lounaita(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kateisosto_lisaa_lounaita(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_riittamaton_maukas_kateisosto_ei_lisaa_rahaa_kassaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_riittamaton_edullinen_kateisosto_ei_lisaa_rahaa_kassaan(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_riittamaton_maukas_kateisosto_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_riittamaton_edullinen_kateisosto_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_riittamanton_maukas_kateisosto_ei_lisaa_lounasta(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_riittamanton_edullinen_kateisosto_ei_lisaa_lounasta(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukas_osto_veloitetaan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

    def test_edullinen_osto_veloitetaan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")

    def test_maukas_korttiostos_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_edullinen_korttiostos_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_maukas_korttiostos_lisaa_lounaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullinen_korttiostos_lisaa_lounaan(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortin_saldo_ei_muutu_maukas_riittamanton(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 2.00 euroa")

    def test_kortin_saldo_ei_muutu_edullinen_riittamanton(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 2.00 euroa")

    def test_riittamaton_maukas_korttiosto_palauttaa_false(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
        
    def test_riittamaton_edullinen_korttiosto_palauttaa_false(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

    def test_riittamaton_maukas_korttiosto_ei_lisaa_lounaita(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_riittamaton_edullinen_korttiosto_ei_lisaa_lounaita(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_maukas_korttiosto_ei_muuta_kassan_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullinen_korttiosto_ei_muuta_kassan_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_riittamaton_maukas_korttiosto_ei_muuta_kassan_saldoa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_riittamaton_edullinen_korttiosto_ei_muuta_kassan_saldoa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_rahan_lataaminen_kortille_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")
    
    def test_rahan_lataaminen_kortille_kasvattaa_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kassasta_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)