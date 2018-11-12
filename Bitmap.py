import numpy as np


class Bitmap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.components = np.empty(self.width * self.height * 4)

    def clear(self, shade):
        # fill array with shade values
        self.components.fill(shade)

    def draw_pixel(self, x, y, a, r, g, b):
        # get index for that pixel
        index = (x + y * self.width) * 4
        self.components[index] = a
        self.components[index+1] = r
        self.components[index+2] = g
        self.components[index+3] = b

    def copy_to_array(self, dest):
        for i in range(self.width*self.height):
            dest[i] = self.components[i + 1]
            dest[i+1] = self.components[i + 2]
            dest[i+2] = self.components[i + 3]