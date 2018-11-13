import numpy as np
import pygame

from Vertex import Vertex


class RenderContext:
    def __init__(self, texture, width, height):
        self.scanBuffer = np.zeros(height*2)
        self.texture = texture

    def draw_scanbuffer(self, yCoordinate, xMin, xMax):
        self.scanBuffer[yCoordinate*2] = xMin
        self.scanBuffer[yCoordinate*2 + 1] = xMax

    def fill_shape(self, yMin, yMax):
        for j in range(yMin, yMax):
            xMin = (int)(self.scanBuffer[j*2])
            xMax = (int)(self.scanBuffer[j*2+1])

            for i in range(xMin, xMax):
                self.texture.set_at((i,j), pygame.Color(255,255,255))

    def fill_triangle(self, v1, v2, v3):
        minYVert = v1
        midYVert = v2
        maxYVert = v3

        if maxYVert.get_y() < midYVert.get_y():
            maxYVert, midYVert = midYVert, maxYVert

        if midYVert.get_y() < minYVert.get_y():
            midYVert, minYVert = minYVert, midYVert

        if maxYVert.get_y() < midYVert.get_y():
            maxYVert, midYVert = midYVert, maxYVert

        area = minYVert.triangle_area2times(maxYVert, midYVert)
        handedness = 1 if (area >= 0) else 0

        self.scan_convert_triangle(minYVert, midYVert, maxYVert, handedness)
        self.fill_shape(100, 300)

    def scan_convert_triangle(self, minYVert, midYVert, maxYVert, handedness):
        self.scan_convert_line(minYVert, maxYVert, 0 + handedness)
        self.scan_convert_line(minYVert, midYVert, 1 - handedness)
        self.scan_convert_line(midYVert, maxYVert, 1 - handedness)

    def scan_convert_line(self, minYVert, maxYVert, whichSide):
        yStart = (int)(minYVert.get_y())
        yEnd = (int)(maxYVert.get_y())
        xStart = (int)(minYVert.get_x())
        xEnd = (int)(maxYVert.get_x())

        yDist = yEnd - yStart
        xDist = xEnd - xStart

        if yDist <= 0:
            return 0

        xStep = xDist/yDist
        currX = xStart

        for j in range(yStart, yEnd):
            self.scanBuffer[j*2 + whichSide] = (int)(currX)
            currX += xStep