class Foo:
    # Как будто бы тут написано
    def __init__(self):
        pass 


    def __init__(self, var_x:int = 0, var_y:int=0):
        self.x = var_x 
        self.y = var_y
    # Будет действительным конструктором т.к. определен последним
    def __init__(self):
        self.x = 10
        self.y = 20

print(dir(Foo()))

def buzz():
    print("First Buzz")

def buzz(a=0):
    print("Second buzz")


buzz()

f = Foo()
print("X is:", f.x)