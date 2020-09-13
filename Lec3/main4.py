class Point:
    x = 0.0
    y = 0.0


def length(p1:Point, p2:Point) -> float:
    """
    Возвращает длину отрезка p1p2
    """
    delta_x = p1.x - p2.x 
    delta_y = p1.y - p2.y 

    return (delta_x**2 + delta_y**2) ** 0.5

def point_creator(arg_x:float, arg_y:float) -> Point:
    p = Point()
    p.x = arg_x
    p.y = arg_y 
    return p

p1 =point_creator(10, 15)

p2 = point_creator(20, 35)

print("Length is:", length(p1, p2))

