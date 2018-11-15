import pygame
import numpy as np
import random
import math


class Star3D:
    def __init__(self, numStars, spread, speed):
        self.spread = spread
        self.speed = speed

        self.starY = np.zeros(numStars)
        self.starZ = np.zeros(numStars)
        self.starX = np.zeros(numStars)

        for i in range(len(self.starX)):
            self.init_star(i)

    def init_star(self, index):
        self.starX[index] = 2 * (random.uniform(0, 1) - 0.5) * self.spread
        self.starY[index] = 2 * (random.uniform(0, 1) - 0.5) * self.spread
        self.starZ[index] = (random.uniform(0,1) + 0.00001) * self.spread

    def update_and_render(self, target, delta):
        target.fill(pygame.Color(0,0,0))
        target.set_at((200, 300), pygame.Color(255, 0, 0, 255))

        halfwidth = target.get_width()/2.0
        halfheight = target.get_height()/2.0

        tanHalfFOV = math.tan(math.radians(70.0/2.0))

        for i in range(len(self.starX)):
            self.starZ[i] -= delta * self.speed

            if self.starZ[i] <= 0:
                self.init_star(i)

            x = (int)((self.starX[i]/self.starZ[i] * tanHalfFOV) * halfwidth + halfwidth)
            y = (int)((self.starY[i]/self.starZ[i] * tanHalfFOV) * halfheight + halfheight)

            if (x < 0 or x >= target.get_width()) or (y < 0 or y >= target.get_height()):
                self.init_star(i)
            else:
                target.set_at((x, y), pygame.Color(255, 0, 0, 255))
