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
        

class Rectangle(BaseFigure):
    color = "RED RECTANGLE"

r = Rectangle()
print("Color:", r.color)

bf = BaseFigure()
print(isinstance(bf, Rectangle))

# Показывает, КАКОГО ТИПА ЭТОТ ОБЪЕКТ
print(type(r))
# Чтобы ответить на вопрос : был ли порожден объект r инструкцией Rectangle
print( isinstance(r, BaseFigure))