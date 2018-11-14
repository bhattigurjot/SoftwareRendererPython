import numpy as np
from Vector4f import Vector4f

class Matrix4f:
    def __init__(self):
        self.m = np.zeros((4,4))

    def get_matrix(self):
        return self.m

    def set_matrix(self, m):
        self.m = m

    def get_value_at(self, i, j):
        return self.m[i][j]

    def set_value_at(self, i, j, val):
        self.m[i][j] = val

    def init_identity(self):
        self.m[0][0] = 1
        self.m[1][1] = 1
        self.m[2][2] = 1
        self.m[3][3] = 1
        return self.m

    def matrix_mul(self, mat):
        res = Matrix4f()

        for i in range(0,3):
            for j in range(0,3):
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