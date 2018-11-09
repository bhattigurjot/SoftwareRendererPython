#!/usr/bin/python
import pygame

win = 0


def init():
    global win
    pygame.init()

    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Software Renderer")
    run()


def run():
    global win
    keepRunning = True
    while keepRunning:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepRunning = False

        pygame.draw.rect(win, (255,0,0), (30,40,100,200))
        win.set_at((300, 300), (255,0,0))
        pygame.display.update()

    pygame.quit()


def main():
    init()


if __name__=="__main__":
    main()