# Родительский класс
class BaseFigure:
    # Информация основного класса (базовая заготовка на производстве)
    color = "brown"
    material = "wood"
    price = 10.33
    def nice_print(self):
        print("Figure color:", self.color)
        print("Figure material:", self.material)
        print("Figure price:", self.price)
        

# Дочерний класс
class Circle(BaseFigure):
    
    # Свойства конретно этого объекта
    radius = 10
    def perimeter(self):
        return 2 * 3.14 * self.radius


c = Circle()
c.nice_print()
print("Perimeter:", c.perimeter())