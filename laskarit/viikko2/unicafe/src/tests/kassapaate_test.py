import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassassa_rahaa_aluksi_oikea_maara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_aluksi_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_aluksi_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_osto_kateisella_onnistuu_kun_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaan_osto_kateisella_onnistuu_kun_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisen_osto_ei_onnistu_kun_maksu_liian_pieni(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_osto_ei_onnistu_kun_maksu_liian_pieni(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_korttiosto_onnistuu_kun_kortin_saldo_riittaa(self):
        maksukortti = Maksukortti(300)
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), True)
        self.assertEqual(maksukortti.saldo, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_korttiosto_onnistuu_kun_kortin_saldo_riittaa(self):
        maksukortti = Maksukortti(500)
        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), True)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_korttiosto_ei_onnistu_kun_kortin_saldo_ei_tarpeeksi(self):
        maksukortti = Maksukortti(200)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_korttiosto_ei_onnistu_kun_kortin_saldo_ei_tarpeeksi(self):
        maksukortti = Maksukortti(200)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_toimii(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(maksukortti.saldo, 1000)

    def test_negatiivisen_summan_lataaminen_kortille_ei_onnistu(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(maksukortti.saldo, 0)