from EngineMaths import Vector4f


class Vertex:
    def __init__(self, x, y=None, z=None):
        if y is None:
            self.pos = x
        else:
            self.pos = Vector4f(x, y, z, 1)

    def __str__(self):
        return "Vertex ({0}, {1}, {2})".format(self.pos.x, self.pos.y, self.pos.z)

    def __repr__(self):
        return "<Vertex: x:{0}, y:{1}, z:{2}, w:{3}>".format(self.pos.x, self.pos.y, self.pos.z, self.pos.w)

    def set_x(self, x):
        self.pos.x = x

    def set_y(self, y):
        self.pos.y = y

    def set_z(self, z):
        self.pos.z = z

    def get_x(self):
        return self.pos.x

    def get_y(self):
        return self.pos.y

    def get_z(self):
        return self.pos.z

    def transform(self, mat):
        return Vertex(mat.transform(self.pos))

    def perspective_divide(self):
        return Vertex(Vector4f(self.pos.x/self.pos.w, self.pos.y/self.pos.w, self.pos.z/self.pos.w, self.pos.w))

    def triangle_area2times(self, b, c):
        x1 = b.get_x() - self.pos.x
        y1 = b.get_y() - self.pos.y

        x2 = c.get_x() - self.pos.x
        y2 = c.get_y() - self.pos.y

        return x1*y2 - x2*y1
