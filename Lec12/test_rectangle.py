import unittest
from rectangle import Rectangle
import pytest # Аналог unittest'a с небольшим смузи

class TestRectangle(unittest.TestCase):
    def test_perimeter(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.perimeter(), 60)

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200) 

if __name__ == "__main__":
    unittest.main()