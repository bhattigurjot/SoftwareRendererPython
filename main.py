#!/usr/bin/python

from Display import Display
from Star3D import Star3D
from RenderContext import RenderContext
from Vertex import Vertex


def main():
    display = Display(600, 400, "Software Renderer")
    stars = Star3D(1000, 64.0, 20.0)
    shape = RenderContext(display.get_target(),600,400)

    minYVert = Vertex(100,100)
    midYVert = Vertex(150,200)
    maxYVert = Vertex(80,300)

    while display.is_running():
        display.poll_events()
        # stars.update_and_render(display.get_target(), display.get_delta())

        shape.fill_triangle(midYVert, maxYVert, minYVert)

        display.render()

    display.clean_up()


if __name__=="__main__":
    main()