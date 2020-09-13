# Множественное наследование
class A:
    a = 1

class B:
    b = 1 

class C(B,A):
    c = 1 

c = C()
print("a:", c.a)
print("b:", c.b)
print("c:", c.c)

print("c vs A:", isinstance(c, A))
print("c vs B:", isinstance(c, B))