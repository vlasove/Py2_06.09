# import unittest
# from rectangle import Rectangle

# class TestRectangle(unittest.TestCase):
#     def test_perimeter(self):
#         r = Rectangle(10, 20)
#         self.assertEqual(r.perimeter(), 60)

#     def test_area(self):
#         r = Rectangle(10, 20)
#         self.assertEqual(r.area(), 200) 


class Rectangle:
    def __init__(self, a, b):
        self.__a = a 
        self.__b = b 

    def perimeter(self):
        return 2*(self.__a + self.__b)

    def area(self):
        return self.__a * self.__b 