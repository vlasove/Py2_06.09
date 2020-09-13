# Множество set()

a_set = set([100,1,2,3,4,5,5,5,55,5,5,5,5,1])
print("A_set:", a_set)
print("Length:", len(a_set))

if 22 in a_set:
    print("22 in set()")
else:
    a_set.add(22)
    print(a_set)
    print("22 in set()")


min(a_set)

for elem in a_set:
    print("Current elem:", elem)


a_set = set([1,2,3])
b_set = set([2,3,4])

print("Union:", a_set.union(b_set))
print("Intersection:", a_set.intersection(b_set))
print("Diff:", a_set.difference(b_set))
print("Symmetric difference:", a_set.symmetric_difference(b_set))

