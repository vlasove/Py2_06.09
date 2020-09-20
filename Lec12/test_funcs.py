"""
Требования для создания модульных тестов:
1) Исходный код декомпозирован
2) Файл с тестами начинает со слова `test_`
3) Класс с модульными тестами начинается со слова `Test..`
4) Тествоые методы начинаются со слова `test_`
5) Внутри одного теста описывается минимум 5 test_case

Аксиома модульных тестов:
1) Код работает правильно <=> каждый юнит работает правильно
"""
import unittest
import funcs 

class TestFuncs(unittest.TestCase):
    def test_add(self):
        self.assertEqual(funcs.add(2,3), 5) #test_case
        self.assertEqual(funcs.add(10, -10), 0)
        self.assertEqual(funcs.add(10, 0), 10)
        self.assertEqual(funcs.add(-1, -2), -3)

    def test_sub(self):
        self.assertEqual(funcs.sub(10, 20), -10)
        self.assertEqual(funcs.sub(5,4), 1)
        self.assertEqual(funcs.sub(-2, -3), 1)
        self.assertEqual(funcs.sub(0, 10), -10)

    def test_mult(self):
        pass 

    def method(self):
        pass 

if __name__ == "__main__":
    unittest.main() # вызов фреймворка для тестов