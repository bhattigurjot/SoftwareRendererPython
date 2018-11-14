#!/usr/bin/python

from Display import Display
from Star3D import Star3D
from RenderContext import RenderContext
from Vertex import Vertex
from EngineMaths import Matrix4f

import math


def main():
    display = Display(600, 400, "Software Renderer")
    stars = Star3D(1000, 64.0, 20.0)
    shape = RenderContext(display.get_target(),600,400)

    minYVert = Vertex(-1,-1,0)
    midYVert = Vertex(0,1,0)
    maxYVert = Vertex(1,-1,0)

    # projection matrix
    projection = Matrix4f().init_perspective(math.radians(70.0),
                                             display.get_aspect_ratio(),
                                             0.1, 1000.0)

    rotCounter = 0.0

    while display.is_running():
        display.poll_events()
        # stars.update_and_render(display.get_target(), display.get_delta())

        rotCounter += display.get_delta()
        translation = Matrix4f().init_translation(0.0, 0.0, 3.0)
        rotation = Matrix4f().init_rotation(0.0, rotCounter, 0.0)
        finalTransform = projection * translation * rotation

        # Clear screen to black
        display.get_target().fill((0,0,0))
        # Draw shape
        shape.fill_triangle(midYVert.transform(finalTransform),
                            maxYVert.transform(finalTransform),
                            minYVert.transform(finalTransform))

        display.render()

    display.clean_up()


if __name__=="__main__":
    main()