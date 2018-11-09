import pygame


class Display:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        # initialize pygame
        pygame.init()

        self.display = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(self.title)
        self.running = True

    def run_engine(self):

        while self.running:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.render()

        self.clean_up()

    def render(self):
        pygame.draw.rect(self.display, (255, 0, 0), (30, 40, 100, 200))
        self.display.set_at((300, 300), (255, 0, 0))
        pygame.display.update()

    def clean_up(self):
        pygame.quit()