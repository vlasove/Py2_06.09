from collections import Counter
first = Counter(a=4, b=2, c=0, d=-2)
second = Counter(a=1, b=2, c=3, d=4)


print("+ : ",first + second)
print("- : ", first - second)
print("& : ", first & second)
print("| : ", first | second)