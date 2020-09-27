import collections


names = ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Alex', 'Fedya']
unique = collections.Counter()

for name in names:
    unique[name] += 1

print(unique)


counter = collections.Counter(a=10, b=20, c =0, d=3)
print(list(counter.elements()))


print()
print("##########from list##################")
counter_from_list = collections.Counter(names)
print(counter_from_list)
print("Key: 'Alice', val: ", counter_from_list["Alice"])
for key, val in counter_from_list.items():
    print(key, val)


##### top-N
print(counter_from_list.most_common(1))
