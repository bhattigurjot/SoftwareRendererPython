

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def triangle_area(self, b , c):
        x1 = b.get_x() - self.x
        y1 = b.get_y() - self.y

        x2 = c.get_x() - self.x
        y2 = c.get_y() - self.y

        return (x1*y2 - x2*y1)
