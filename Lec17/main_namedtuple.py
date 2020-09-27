"""
Коллекция, основання на кортеже, предназначена для определния
небольших заименованных полей (структур)
"""
from collections import namedtuple 

Student = namedtuple('Student', ['name', 'age'])
s1 = Student('Bob', 22)
print(s1)

# Наследование от namedtuple запрещено
class NewStudent(Student):
    def __init__(self, name, age, email):
        super().__init__(name, age)
        self.email = email 

ns = NewStudent('Bob', 22, 'bob@mail.ru')
print(ns)