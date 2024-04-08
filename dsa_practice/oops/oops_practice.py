"""
Write oops classes to handle the following scenarios:
A user can create and view 2D coordinates
A user can find out the distance between two coordinates
A user can find the distance of a coordinates from the origin
A user can check if a point lies on a given line
A user can find the distance between a given 2D point and a given line
"""


class Point:

    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y

    def __str__(self):
        return '<{}, {}>'.format(self.x_cord, self.y_cord)

    def euclidian_distance(self, other):
        return ((self.x_cord - other.x_cord) ** 2 + (self.y_cord - other.y_cord) ** 2) ** 0.5

    def distance_from_origin(self):
        # return self.euclidian_distance(Point(0, 0))
        return (self.x_cord ** 2 + self.y_cord ** 2) ** 0.5

    def is_on_line(self, line):
        return self.x_cord * line.y_cord - self.y_cord * line.x_cord == 0

    def distance_to_line(self, line):
        return (self.x_cord * line.y_cord - self.y_cord * line.x_cord) / (line.x_cord ** 2 + line.y_cord ** 2) ** 0.5

    def __eq__(self, other):
        return self.x_cord == other.x_cord and self.y_cord == other.y_cord


# p1 = Point(0, 0)
# p2 = Point(1, 1)
# p1.euclidian_distance(p2)


class Line:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)

    def point_on_line(self, point):
        if self.A*point.x_cord + self.B*point.y_cord + self.C == 0:
            return "Lies on the line"
        else:
            return "Does not lie on the line"

    def shortest_distance(self, point):
        return abs(self.A*point.x_cord + self.B*point.y_cord + self.C) / (self.A*self.A + self.B*self.B) ** 0.5


l1 = Line(1, 1, -2)
p1 = Point(1, 1)
print(l1.shortest_distance(p1))