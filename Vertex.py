from Vector4f import Vector4f


class Vertex:
    def __init__(self, x, y=None):
        if y is None:
            self.pos = x
        else:
            self.pos = Vector4f(x, y, 0, 1)

    def set_x(self, x):
        self.pos.x = x

    def set_y(self, y):
        self.pos.y = y

    def get_x(self):
        return self.pos.x

    def get_y(self):
        return self.pos.y

    def transform(self, mat):
        return Vertex(mat.transform(self.pos))

    def triangle_area2times(self, b, c):
        x1 = b.get_x() - self.pos.x
        y1 = b.get_y() - self.pos.y

        x2 = c.get_x() - self.pos.x
        y2 = c.get_y() - self.pos.y

        return x1*y2 - x2*y1
