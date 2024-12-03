import unittest
from Haromszog import Haromszog

class TestHaromszog(unittest.TestCase):
     def test_szerkesztheto_modositasok(self):
        h = Haromszog(5, 5, 5)
        
        h.SetB(6)
        
        self.assertEqual(h.Kerulet(), 16)


if __name__ == '__main__':

    unittest.main()
