import pygame
# from Bitmap import Bitmap


class Display:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.displayImage = None
        self.displayComponents = None
        # self.frameBuffer = None
        self.clock = pygame.time.Clock()
        self.timedelta = 1.0

        # initialize pygame
        pygame.init()

        self.display = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(self.title)
        self.running = True

        # self.frameBuffer = Bitmap(self.width, self.height)
        self.displayComponents = pygame.Surface((self.width,self.height)).get_buffer()
        self.displayImage = pygame.image.frombuffer(self.displayComponents, (self.width,self.height), 'RGBA')

    def poll_events(self):
        # poll all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):
        self.timedelta = self.clock.tick(60) / 1000  # convert to milliseconds

        # blit to surface
        self.display.blit(self.displayImage, (0, 0))

        pygame.display.update()

    def clean_up(self):
        pygame.quit()

    def get_delta(self):
        return self.timedelta

    def get_target(self):
        return self.displayImage

    def is_running(self):
        return self.running