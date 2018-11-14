import math
from Vector4f import Vector4f


class Quaternion:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w)

    def normalized(self):
        length = self.length()
        return Quaternion(self.x/length, self.y/length, self.z/length, self.w/length)

    def normalize_this(self):
        length = self.length()
        self.x /= length
        self.y /= length
        self.z /= length
        self.w /= length
        return self

    def conjugate(self):
        return Quaternion(-self.x, -self.y, -self.z, -self.w)

    def mul(self, other):
        if other is Quaternion:
            _w = self.w*other.w - self.x*other.x - self.y*other.y - self.z*other.z
            _x = self.x*other.w + self.w*other.x + self.y*other.z - self.z*other.y
            _y = self.y*other.w + self.w*other.y + self.z*other.x - self.x*other.z
            _z = self.z*other.w + self.w*other.z + self.x*other.y - self.y*other.x
            return Quaternion(_x, _y, _z, _w)
        if other is Vector4f:
            _w = -self.x * other.x - self.y * other.y - self.z * other.z
            _x = self.w * other.x + self.y * other.z - self.z * other.y
            _y = self.w * other.y + self.z * other.x - self.x * other.z
            _z = self.w * other.z + self.x * other.y - self.y * other.x
            return Quaternion(_x, _y, _z, _w)