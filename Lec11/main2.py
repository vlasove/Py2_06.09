# Импортирование класса
from triangle import Triangle



# Импортирование функции непривязанной к классу
from triangle import figure_logger

t = Triangle()
# Вызов статик метода
t.figure_logger()
Triangle.figure_logger()