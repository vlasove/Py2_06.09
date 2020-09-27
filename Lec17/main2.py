from collections import namedtuple

class Point:
    def __init__(self, x, y):
        self.__x = x 
        self.__y = y 

    def __str__(self):
        return "Point <X:{} Y:{}>".format(self.__x, self.__y)

p = Point(10, 20)
print("Point: ", p)

NewPoint = namedtuple('NewPoint', ['x', 'y'])
np = NewPoint(x=1, y=2)
print(type(NewPoint))
print("NewPoint: ", np)
print(np.x, np.y)
print(np[0], np[1])
print(dir(np))


