import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luodun_kortin_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataa_rahaa_toimii(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_ota_rahaa_toimii_kun_saldoa_riittavasti(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo, 500)

    def test_ota_rahaa_ei_muuta_saldoa_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_ota_rahaa_palautta_true_kun_rahat_riittivat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_ota_rahaa_palauttaa_false_kun_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)

    def test_tulostus_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")