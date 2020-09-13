class Point:
    def __init__(self, var_x:int=0, var_y:int =0):
        self.x = var_x 
        self.y = var_y 

    def __str__(self):
        return "<Point[X:{}, Y{}]".format(self.x, self.y)
    
    # Деструктор - это метод, который вызывается при передаче 
    # объекта сборщику мусора (Garbage Collector)
    def __del__(self):
        pass 
