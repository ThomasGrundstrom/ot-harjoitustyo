import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.__str__(), "Kortilla on rahaa 10.00 euroa")
    
    def test_saldon_kasvattaminen_toimii(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(self.maksukortti.__str__(), "Kortilla on rahaa 35.00 euroa")
    
    def test_saldo_vahenee_oikein(self):
        self.assertEqual(self.maksukortti.ota_rahaa(250), True)
        self.assertEqual(self.maksukortti.ota_rahaa(2500), False)