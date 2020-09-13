nums = [10, 20, 30, 40, 50]

print("Before deleting: ELEMS-", nums, "W:", nums.__sizeof__(), "bytes")
del nums[-1]
print("After deleting: ELEMS-", nums, "W:", nums.__sizeof__(), "bytes")