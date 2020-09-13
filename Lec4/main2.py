class Point:
    x = 0.0 
    y = 0.0 

    def printer(self):
        print("<X>:", self.x, "<Y>:", self.y)

    def __str__(self):
        return "Point<X:" + str(self.x) + ", Y:"+str(self.y) +" >"

p = Point()
p.x, p.y = 10, 20
p2 = Point()
p2.x , p2.y = 200, 300

p.printer()
print([p,  p2])
print(dir(p))


# a = 10
# print(a) a.__repr__() / a.__str__()