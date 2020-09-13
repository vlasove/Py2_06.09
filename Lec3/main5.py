class Point:
    x = 0.0
    y = 0.0


def length(p1:Point, p2:Point) -> float:
    delta_x = p1.x - p2.x 
    delta_y = p1.y - p2.y 

    return (delta_x**2 + delta_y**2) ** 0.5

def perimeter_triangle(p1:Point, p2:Point, p3:Point) -> float:
    """
    Считает периметр треугольника на точках p1p2p3 
    """
    side_a = length(p1,p2)
    side_b = length(p2, p3)
    side_c = length(p3, p1)
    return side_a + side_b + side_c

def area_triangle(p1:Point, p2:Point, p3:Point) -> float:
    """
    Считает площадь труегольника на точках p1p2p3
    S = sqrt(p(p-a)(p-b)(p-c))
    """
    p = perimeter_triangle(p1, p2, p3) / 2
    s = (p*(p-length(p1,p2)) * (p - length(p2,p3)) * (p-length(p1,p3))) ** 0.5 
    return s


def point_creator(arg_x:float, arg_y:float) -> Point:
    p = Point()
    p.x = arg_x
    p.y = arg_y 
    return p


p1, p2, p3 = point_creator(0,0), point_creator(0, 10), point_creator(10, 0)
print("Perimeter:", perimeter_triangle(p1, p2, p3))
print("Area:", area_triangle( p1, p2, p3))