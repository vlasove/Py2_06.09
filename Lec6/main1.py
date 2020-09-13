nums = [x for x in range(1, 1000)] # List comprehension
while len(nums) > 1:
    if len(nums) % 10 == 0:
        print("W:", nums.__sizeof__(), "Len:", len(nums))
    
    del nums[-1]

print("GC")