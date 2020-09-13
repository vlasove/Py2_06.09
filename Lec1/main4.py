def my_func(a:int, b:int) -> int:
    """
    This function for add of two vals
    """
    return a**2 + b 

def second_func(message:str = "default", num:int):
    print("Hey")
    print("Message:", message)

res1 = my_func(2,3)
res2 = second_func()

print('Result 1:', res1)
print("Result 2:", res2)

second_func()
second_func("abcd")

anon = lambda x,y : x + y
anon(2,3)
