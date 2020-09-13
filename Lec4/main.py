# Класс - инструкция порождения новых сущностей одного типа.

class Point:
    x = 0.0 # !!!атрибут!!! класса Point / поле класса Point / свойство класса Point
    y = 0.0
    
    # Метод класса Point // self - получатель метода
    def nice_print(self):
        """
        ЭТА ФУНКЦИЯ РАБОТАЕТ ТОЛЬСКО С ПРЕДСТАВИТЕЛЯМИ КЛАССА POINT
        """
        print("<X>:", self.x)
        print("<Y>:", self.y)

p1 = Point() # объект класса Point / экземпляр класса Point
p1.x = 10
p1.y = 12


p2 = Point()
p2.x, p2.y= 100, 100

p1.nice_print()
p2.nice_print()


