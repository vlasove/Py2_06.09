class Point:
    """
    This class for .....
    Эта строка документации класса 
    """
    # Constructor правильный (параметризованный конструктор)
    def __init__(self, var_x:int = 0, var_y:int = 0):
        print("Construct works")
        self.x = var_x  
        self.y = var_y 
        print("Construct finished")
        # У этого атрибута нет изначального параметра, приходящего из аргументов конструктора
        self.is_valid = False 

    def __str__(self):
        return "<Point [X:{}, Y:{}]>".format(self.x, self.y)

    def something_method(self):
        """
        Обязательно нужно описать что это, для чего это, и что оно делает
        """
        pass 

p = Point(10, 20)
print(p)
p1 = Point()
print(p1)

    