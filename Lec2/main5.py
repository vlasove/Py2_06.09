a_list = [2,3,4,5,6,7]

b_list = a_list.copy()
b_list.append(2000)

print("a_list:", a_list)
print("b_list:", b_list)
# Изменяет состояние текущего списка
a_list.sort()

#Возвращает новый список на основе предыдущего
new_list = sorted(a_list)