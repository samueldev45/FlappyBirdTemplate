import pygame
from Lib.Window import Window

class Application:
    def __init__(self):
        self.window = Window(self)
        self.window.create(800, 600, "Flappy Bird Template")
        self.fps = 60

        self.__running = False
        self.__clock = pygame.time.Clock()

    # game loop
    def run(self):
        self.__running = True

        while self.__running:
            self.window.events()
            self.window.update()
            self.window.render()

            pygame.display.update()
            self.__clock.tick(self.fps)
        pygame.quit()

    def close(self):
        self.__running = False