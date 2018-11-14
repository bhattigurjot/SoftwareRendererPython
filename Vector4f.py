import math


class Vector4f:
    def __init__(self, x, y, z, w=1.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z + self.w*self.w)

    def normalized(self):
        length = self.length()
        return Vector4f(self.x/length, self.y/length, self.z/length, self.w/length)

    def dot_product(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z + self.w*other.w

    def cross_product(self, other):
        _x = self.y*other.z - self.z*other.y
        _y = self.z*other.x - self.x*other.z
        _z = self.x*other.y - self.y*other.x
        return Vector4f(_x,_y,_z,0)

    def rotate(self, angle):
        sinAngle = math.sin(-angle)
        cosAngle = math.cos(-angle)

        # return self.cross()

    def equals(self, other):
        return self.x == other.x && self.y == other.y && self.z == other.z && self.w == other.w

    def add(self, other):
        if other is float:
            return self.x + other, self.y + other, self.z + other, self.w + other
        else:
            return Vector4f(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def sub(self, other):
        if other is float:
            return self.x - other, self.y - other, self.z - other, self.w - other
        else:
            return Vector4f(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def mul(self, other):
        if other is float:
            return self.x * other, self.y * other, self.z * other, self.w * other
        else:
            return Vector4f(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)

    def div(self, other):
        if other is float:
            return self.x / other, self.y / other, self.z / other, self.w / other
        else:
            return Vector4f(self.x / other.x, self.y / other.y, self.z / other.z, self.w / other.w)

    def abso(self):
        return Vector4f(math.fabs(self.x), math.fabs(self.y), math.fabs(self.z), math.fabs(self.w))
