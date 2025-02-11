class Shape(object):
    def __init__(self):
        pass


class Rectangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self)
        self.length = l
        self.width=w

    def area(self):
        return self.length*self.width

rectangle= Rectangle(3, 5)
print(rectangle.area())