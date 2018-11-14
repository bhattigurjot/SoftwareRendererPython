import math
import numpy as np


class Vector4f:
    def __init__(self, x, y, z, w=1.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def __str__(self):
        return "Vector4f ({0}, {1}, {2}, {3})".format(self.x, self.y, self.z, self.w)

    def __repr__(self):
        return "<Vector4f: x:{0}, y:{1}, z:{2}, w:{3}>".format(self.x, self.y, self.z, self.w)

    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z + self.w*self.w)

    def normalized(self):
        length = self.length()
        return Vector4f(self.x/length, self.y/length, self.z/length, self.w/length)

    def dot_product(self, vec):
        return self.x*vec.x + self.y*vec.y + self.z*vec.z + self.w*vec.w

    def cross_product(self, vec):
        _x = self.y*vec.z - self.z*vec.y
        _y = self.z*vec.x - self.x*vec.z
        _z = self.x*vec.y - self.y*vec.x
        return Vector4f(_x,_y,_z,0)

    def rotate(self, angle):
        sinAngle = math.sin(-angle)
        cosAngle = math.cos(-angle)

        # return self.cross()

    def equals(self, vec):
        return self.x == vec.x and self.y == vec.y and self.z == vec.z and self.w == vec.w

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector4f(self.x + other, self.y + other, self.z + other, self.w + other)
        else:
            return Vector4f(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector4f(self.x - other, self.y - other, self.z - other, self.w - other)
        else:
            return Vector4f(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector4f(self.x * other, self.y * other, self.z * other, self.w * other)
        else:
            return Vector4f(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector4f(self.x / other, self.y / other, self.z / other, self.w / other)
        else:
            return Vector4f(self.x / other.x, self.y / other.y, self.z / other.z, self.w / other.w)

    def abso(self):
        return Vector4f(math.fabs(self.x), math.fabs(self.y), math.fabs(self.z), math.fabs(self.w))


class Matrix4f:
    def __init__(self):
        self.m = np.zeros((4,4))

    def __str__(self):
        return "Matrix4f\n {0}".format(self.m)

    def __repr__(self):
        return "<Matrix4f\n {0}>".format(self.m)

    def get_matrix(self):
        return self.m

    def set_matrix(self, m):
        self.m = m

    def get_value_at(self, i, j):
        return self.m[i][j]

    def set_value_at(self, i, j, val):
        self.m[i][j] = val

    def init_screenspace_transform(self, halfWidth, halfheight):
        self.m[0][0] = halfWidth
        self.m[0][3] = halfWidth
        self.m[1][1] = -halfheight
        self.m[1][3] = halfheight
        self.m[2][2] = 1
        self.m[3][3] = 1
        return self

    def init_identity(self):
        self.m[0][0] = 1
        self.m[1][1] = 1
        self.m[2][2] = 1
        self.m[3][3] = 1
        return self

    def init_translation(self, x, y, z):
        self.m[0][0] = 1
        self.m[0][3] = x
        self.m[1][1] = 1
        self.m[1][3] = y
        self.m[2][2] = 1
        self.m[2][3] = z
        self.m[3][3] = 1
        return self

    def init_rotation(self, x, y, z):
        rx = Matrix4f()
        ry = Matrix4f()
        rz = Matrix4f()

        rz.m[0][0] = math.cos(z)
        rz.m[0][1] = -math.sin(z)
        rz.m[1][0] = math.sin(z)
        rz.m[1][1] = math.cos(z)
        rz.m[2][2] = 1
        rz.m[3][3] = 1

        rx.m[0][0] = 1
        rx.m[1][1] = math.cos(x)
        rx.m[1][2] = -math.sin(x)
        rx.m[2][1] = math.sin(x)
        rx.m[2][2] = math.cos(x)
        rx.m[3][3] = 1

        ry.m[0][0] = math.cos(y)
        ry.m[0][2] = -math.sin(z)
        ry.m[1][1] = 1
        ry.m[2][0] = math.sin(z)
        ry.m[2][2] = math.cos(x)
        ry.m[3][3] = 1

        self.m = (rz * (ry * rx)).get_matrix()

        return self

    def init_perspective(self, fov, aspect_ratio, zNear, zFar):
        tanHalfFOV = math.tan(fov / 2)
        zRange = zNear - zFar

        self.m[0][0] = 1.0 / (tanHalfFOV * aspect_ratio)
        self.m[1][1] = 1.0 / tanHalfFOV
        self.m[2][2] = (-zNear - zFar) / zRange
        self.m[2][3] = 2 * zFar * zNear / zRange
        self.m[3][2] = 1

        return self

    def __mul__(self, mat):
        res = Matrix4f()

        for i in range(0,4):
            for j in range(0,4):
                val = (self.m[i][0] * mat.get_value_at(0, j))
                val += (self.m[i][1] * mat.get_value_at(1, j))
                val += (self.m[i][2] * mat.get_value_at(2, j))
                val += (self.m[i][3] * mat.get_value_at(3, j))

                res.set_value_at(i, j, val)

        return res

    def transform(self, vec):
        return Vector4f(self.m[0][0] * vec.x + self.m[0][1] * vec.y + self.m[0][2] * vec.z + self.m[0][3] * vec.w,
                        self.m[1][0] * vec.x + self.m[1][1] * vec.y + self.m[1][2] * vec.z + self.m[1][3] * vec.w,
                        self.m[2][0] * vec.x + self.m[2][1] * vec.y + self.m[2][2] * vec.z + self.m[2][3] * vec.w,
                        self.m[3][0] * vec.x + self.m[3][1] * vec.y + self.m[3][2] * vec.z + self.m[3][3] * vec.w)


class Quaternion4f:
    def __init__(self, x, y, z, w):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def __str__(self):
        return "Quaternion4f ({0}, {1}, {2}, {3})".format(self.x, self.y, self.z, self.w)

    def __repr__(self):
        return "<Quaternion4f: x:{0}, y:{1}, z:{2}, w:{3}>".format(self.x, self.y, self.z, self.w)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w)

    def normalized(self):
        length = self.length()
        return Quaternion4f(self.x/length, self.y/length, self.z/length, self.w/length)

    def normalize_this(self):
        length = self.length()
        self.x /= length
        self.y /= length
        self.z /= length
        self.w /= length
        return self

    def conjugate(self):
        return Quaternion4f(-self.x, -self.y, -self.z, -self.w)

    def mul(self, other):
        if other is Quaternion4f:
            _w = self.w*other.w - self.x*other.x - self.y*other.y - self.z*other.z
            _x = self.x*other.w + self.w*other.x + self.y*other.z - self.z*other.y
            _y = self.y*other.w + self.w*other.y + self.z*other.x - self.x*other.z
            _z = self.z*other.w + self.w*other.z + self.x*other.y - self.y*other.x
            return Quaternion4f(_x, _y, _z, _w)
        if other is Vector4f:
            _w = -self.x * other.x - self.y * other.y - self.z * other.z
            _x = self.w * other.x + self.y * other.z - self.z * other.y
            _y = self.w * other.y + self.z * other.x - self.x * other.z
            _z = self.w * other.z + self.x * other.y - self.y * other.x
            return Quaternion4f(_x, _y, _z, _w)