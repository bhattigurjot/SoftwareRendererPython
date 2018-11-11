import numpy as np


class Bitmap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.components = np.empty(self.width * self.height * 4)

    def clear(self, shade):
        # fill array with shade values
        self.components.fill(shade)

    def draw_pixel(self, x, y, a, b, g, r):
        # get index for that pixel
        index = (x + y * self.width) * 4
        self.components[index] = a
        self.components[index+1] = b
        self.components[index+2] = g
        self.components[index+3] = r