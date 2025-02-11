import math

class Point(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        print(({self.x}, {self.y}))

    def move(self, x_1, y_1):
        self.x+=x_1
        self.y+=y_1

    def dist(self, other_point):
        return math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2)
    
point1 = Point(3, 4)
point2 = Point(6, 8)
point1.show()
point1.move(5, 7)
point1.show()
print( point1.dist(point2))
