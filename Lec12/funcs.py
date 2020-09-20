def add(a:int, b:int) -> int:
    """
    Func for addition
    """
    return a + b


def sub(a:int, b:int) -> int:
    """
    Func for substraction
    """
    return a - b

def mult(a:int, b:int) -> int:
    """
    Funcs for multiplication
    """
    return a * b * 4



if __name__ == "__main__":
    print(add(2,3) + sub(10, 20) + mult(20, 30))