import pickle

class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y 

    def __str__(self):
        return "Point<X:{} Y:{}>".format(self.__x, self.__y)

my_points = {"first" : Point(10, 20), "list_point" : [Point(2,3), Point(3,4)]}

with open('data.pickle', 'wb') as fhand:
    pickle.dump(my_points, fhand)
del my_points

ans = None
with open('data.pickle', 'rb') as fhand:
    ans = pickle.load(fhand)

print(ans, type(ans))
for key, val in ans.items():
    print(key, "|||", val)
print(ans["first"])
print(ans["list_point"][0])

