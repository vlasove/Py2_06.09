class Point:
    """
    This class docstring
    """
    def __init__(self, var_x:int=0, var_y:int =0):
        self.x = var_x 
        self.y = var_y 

    def __str__(self):
        return "<Point[X:{}, Y{}]".format(self.x, self.y)
    
    # Деструктор - это метод, который вызывается при передаче 
    # объекта сборщику мусора (Garbage Collector)
    def __del__(self):
        print("Destructor works")
        print(self)
        print("Destructor finished")


def foo():
    p3 = Point(1,1)
    print("In func foo!")
foo()
p = Point(10, 20)
del p # Передача объекта p сборщику мусора
p2 = Point()
print("IN MAIN.PY")
print(1/0)

https://github.com/vlasove/Py2_06.09
https://contest.yandex.ru/contest/19766

D