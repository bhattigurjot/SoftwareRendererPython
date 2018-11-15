import math


class Edge:
    def __init__(self, minYVert, maxYVert):
        self.yStart = int(math.ceil(minYVert.get_y()))
        self.yEnd = int(math.ceil(maxYVert.get_y()))
        self.xStart = int(math.ceil(minYVert.get_x()))
        self.xEnd = int(math.ceil(maxYVert.get_x()))
        self.xStep = 0

        yDist = maxYVert.get_y() - minYVert.get_y()
        xDist = maxYVert.get_x() - minYVert.get_x()

        yPreStep = self.yStart - minYVert.get_y()

        if yDist <= 0.0:
            self.xStep = self.xStep
        else:
            self.xStep = xDist/yDist
        self.x = self.xStart + yPreStep * self.xStep

    def step(self):
        self.x += self.xStep

    def get_x(self):
        return self.x

    def get_y_start(self):
        return int(self.yStart)

    def get_y_end(self):
        return int(self.yEnd)