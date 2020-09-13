# Link to git
# https://github.com/vlasove/Py2_06.09

class Point:
    # Constructor правильный (не параметризованный конструктор)
    def __init__(self):
        print("Construct works")
        self.x = 0.0  # Атрибут х создается в момент обращения через self
        self.y = 0.0 
        print("Construct finished")

    def __str__(self):
        return "<Point [X:{}, Y:{}]>".format(self.x, self.y)
    # Constructor (по функционалу ок, по сути - плохо)
    def point_creator(self, x:int, y:int):
        p = Point()
        p.x , p.y = x, y 
        return p

p = Point()
print(p)
    