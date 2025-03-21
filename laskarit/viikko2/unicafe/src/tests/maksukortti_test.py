import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_saldon_kasvatus_oikein(self):
        self.maksukortti.lataa_rahaa(250)
        self.assertEqual(self.maksukortti.saldo, 1250)

    def test_rahan_ottaminen_oikein(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(self.maksukortti.saldo, 750)
    
    def test_saldo_euroina_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_str_palauttaa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_saldo_pienempi_kuin_maara_oikein(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)