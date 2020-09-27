"""
Словарь со значением по умолчанию.
Определяет ZeroValue для любого значения в словаре
"""
from collections import defaultdict 

nums = defaultdict(int)
nums["one"] = 1
nums["two"] = 2
print(nums["three"])
print(nums)