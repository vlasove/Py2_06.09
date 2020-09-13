class A:
    a = 1
    word = "word from A"

class B:
    b = 1 
    word = "word from B"
# Приоритетное множественное наследование
class C(A,B):
    c = 1 

c = C()
print(c.word) # Что будет распечатано?