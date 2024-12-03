import unittest
from Haromszog import Haromszog, NemSzerkesztheto

class TestHaromszog(unittest.TestCase):
    def test_kerulet_es_terulet(self):
        # Helyes háromszög, ellenőrizzük a kerületet és a területet
        h = Haromszog(3, 4, 5)
        self.assertEqual(h.Kerulet(), 12)
        self.assertAlmostEqual(h.Terulet(), 6.0, places=5)

    def test_szerkesztheto_allapot(self):
        h = Haromszog(3, 4, 5)
        # Érvényes módosítás
        h.SetA(6)
        self.assertEqual(h.a, 6)

        # Nem szerkeszthető állapot (a > b + c)
        with self.assertRaises(NemSzerkesztheto):
            h.SetA(15)
        self.assertEqual(h.a, 6)  # Az érték nem változott

    def test_szerkesztheto_modositasok(self):
        h = Haromszog(5, 5, 5)
        h.SetB(6)  # Érvényes
        self.assertEqual(h.b, 6)

        # Hibás szerkesztés
        with self.assertRaises(NemSzerkesztheto):
            h.SetC(20)
        self.assertEqual(h.c, 5)  # Az érték nem változott


if __name__ == '__main__':

    unittest.main()