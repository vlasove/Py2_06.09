# 3) Полиморфизм - свойство объектов, вести себя по-разному в зависимости от окружения

class Circle:
    def __init__(self, R:int=0):
        self.r = R 
    
    def perimeter(self):
        """
        Периметр окружности
        """
        return 2 * 3.14 * self.r 

    def area(self):
        """
        Площадь окружности. Полиморфный метод
        """
        return 3.14 * self.r ** 2  

class Rectangle:
    def __init__(self, A:int=0, B:int=0):
        self.width = A 
        self.length = B 

    def perimeter(self):
        """
        Периметр прямоугольника
        """
        return 2 * (self.width + self.length)

    def area(self):
        """
        Площадь прямоугольника. Полиморфный метод
        """
        return self.width * self.length 

class Triangle:
    def __init__(self, a:int=0, b:int=0, c:int=0):
        self.side_a = a 
        self.side_b = b 
        self.side_c = c 

    def area(self):
        """
        Формула Герона должна быть. Полиморфный метод
        """
        return self.side_a * self.side_b * self.side_c

c1 = Circle(10)
c2 = Circle(30)
c3 = Circle(15)

r1 = Rectangle(10, 20)
r2 = Rectangle(50, 50)

t1 = Triangle(1,2,3)
t2 = Triangle(3,4,5)



print("Circle area:", c1.area())
print("Rectangle area:", r1.area()) 

# Задача - подсчитать общую площадь, которую занимают эти фигуры на странице
figures = [c1, c2 ,c3, r1, r2, t1, t2]


total_area = 0
for fig in figures:
    total_area += fig.area()


# rectangles = [r1, r2]
# Rectangle_total_area = 0
# for rectangle in rectangles:
#     Rectangle_total_area += rectangle.area_rectangle()

# triangles = [t1, t2]