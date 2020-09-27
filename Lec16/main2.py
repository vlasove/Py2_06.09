"""
Попытка сериализовать функцию
"""
import pickle 

def add(x:int, y:int) -> int:
    """
    addition
    """
    return x + y 

with open("func.pickle", "wb") as fhand:
    pickle.dump(add, fhand)



new_add = None
with open('func.pickle', 'rb') as fhand:    
    new_add = pickle.load(fhand)

print('Result:', new_add(2,3))
print(new_add, type(new_add))