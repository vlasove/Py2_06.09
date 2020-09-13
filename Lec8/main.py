# 2) Наследование - свойство объектов передавать информацию о себе всем последующим объектам.
# Причем базовый объект (имеющий информацию) - родительский.
# Принимающий информацию - дочерний.

class BaseFigure:
    # Информация основного класса (базовая заготовка на производстве)
    color = "black"
    material = "wood"
    price = 10.22


class Circle:
    # Информация из основного класса
    color = "black"
    material = "wood"
    price = 10.22
    # Свойства конретно этого объекта
    radius = 10


c = Circle()
print("Circle color:", c.color)
print("Circle material:", c.material)
print("Circle radius:", c.radius)