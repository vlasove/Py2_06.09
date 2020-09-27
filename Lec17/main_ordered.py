"""
Словарь с сохранением порядка добавления элементов.
Можно изменять порядок следования элементов при помощи move_to_end()
"""

from collections import OrderedDict

od = OrderedDict()
od['a'], od['b'], od['c'] = 1,2,3
print(od)
od.move_to_end('a')

#od[100] = ['x', 'y']
# Работает точно также как обычный словарь
for key, val in od.items():
    print(key, val)

#pair = od.pop('a')
#print(pair)

print("Size:", od.__sizeof__(), "bytes")
d = {'a':1, 'b':2, "c":3}
print("Size(d):", d.__sizeof__(), "bytes")