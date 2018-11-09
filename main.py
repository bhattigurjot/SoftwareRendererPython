#!/usr/bin/python

from Display import Display

def main():
    display = Display(600, 400, "Software Renderer")
    display.run_engine()


if __name__=="__main__":
    main()