# D2: G pre-solution
# Организовываем ввод 
with open("input.txt", "r") as fhand:
    line = fhand.read() #"1 20 3"
    line = line.strip() # ['1', '20', '3']
    coeffs = [float(elem) for elem in line ]


def solve(a:float, b:float, c:float) -> int:
    """
    Возвращает количество корней квадратного уравнения с коэ
    ффициентами a,b,c
    """
    pass 

# Делаем вывод в файл
with open("output.txt", "w") as fhand:
    fhand.write(str(solve(coeffs[0], coeffs[1], coeffs[0]))) 

#Link: https://contest.yandex.ru/contest/19766/problems/G/