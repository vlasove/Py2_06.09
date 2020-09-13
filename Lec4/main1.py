class Point:
    """
    This class for point emulation
    """
    x = 0.0 
    y = 0.0 
    def line_printer(self, n_counts:int=0):
        line = "<X>:" +str(self.x) + " <Y>:" + str(self.y)
        print(line * n_counts)


    def add_X(self):
        self.x += 1
        # ХОЧУ ВЫЗВАТЬ line printer
        # Способ вызов метода внутри другого метода
        self.line_printer(10)

    def add_Y(self):
        self.y += 1

    def interview(self):
        print(type(self))

    
        

p1 = Point()
p1.x, p1.y = 1, 1

# p1.line_printer(1)
p1.add_X()
# p1.add_Y()
# p1.add_X()
# p1.line_printer(1)

p1.interview()
