"""
Коллекция для объединения наборов словарей в один единый объект
"""

from collections import ChainMap

d1 = {'word1' : 1, 'word2' : 2}
d2 = {'word3' : 3, 'word4': 4}
d3 = {'word5' : 5}

chain_map = ChainMap(d1, d2, d3)
print(chain_map, chain_map.maps)
for key, val in chain_map.items():
    print(key, val)

print(chain_map['word1'] + chain_map['word3'])
print("Keys:", list(chain_map.keys()))
print('Values:', list(chain_map.values()))

# Добавление нового словаря в chain
d4 = {'word6' : 6, 'word7':7}
chain_map = chain_map.new_child(d4)
print("Chain map size:", chain_map.__sizeof__(), "bytes")

total_not_chain = {'word1' : 1, 'word2' : 2, 'word3' : 3, 'word4': 4, 'word5' : 5, 'word6' : 6, 'word7':7}
print("Not chain map size:", total_not_chain.__sizeof__(), "bytes")
