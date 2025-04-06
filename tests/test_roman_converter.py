import unittest

from src.roman_converter import decimalromanos

class TestRomanos(unittest.TestCase):
    def test_numeros_individuales(self):
        self.assertEqual(decimalromanos(1), "I")
        self.assertEqual(decimalromanos(5), "V")
        self.assertEqual(decimalromanos(10), "X")
    
    def test_orden_numeros(self):
        self.assertEqual(decimalromanos(14), "XIV")
        self.assertEqual(decimalromanos(16), "XVI")
        self.assertEqual(decimalromanos(4), "IV")
        self.assertEqual(decimalromanos(6), "VI")
    
    def test_numeros_complejos(self):
        self.assertEqual(decimalromanos(3999), "MMMCMXCIX")
        self.assertEqual(decimalromanos(49), "XLIX")
        self.assertEqual(decimalromanos(99), "XCIX")
        self.assertEqual(decimalromanos(499), "CDXCIX")

if __name__ == "__main__":
    unittest.main()