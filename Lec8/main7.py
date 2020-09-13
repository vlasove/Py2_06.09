class A:
    def __init__(self, a:int=1):
        self.a = a 
        print("Construct from A!")

    def print(self):
        pass 

class B:
    def __init__(self, b:int = 1):
        self.b = b 
        print("Construct from B!")

class C(A,B):
    def __init__(self,a:int=1, b:int=1, c:int = 1):
        # super(). больше не является универсальным инстурментом
        # т.к. в случае 2-ух и более родителей он работает по приоритету
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = c 
        




c = C(1,2,3)
print("c.a: ", c.a)
print("c.b:", c.b)
print("c.c:", c.c)
