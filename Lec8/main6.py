class A:
    a = 1 

class B(A):
    def print(self):
        print("Hello from B:", self.a)

        
class C(A):
    def print(self):
        print("Hello from C:", self.a)

class D(B,C):
    pass 


d = D()
d.print()