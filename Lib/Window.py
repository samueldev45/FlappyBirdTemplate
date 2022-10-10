import pygame

class Window:
    def __init__(self, app):
        # initializing the pygame modules
        if not pygame.get_init():
            pygame.init()

        self.display = None

        self.__app = app

    def create(self, width : int, height : int, title : str, flags : int = 0, vsync : bool = False):
        self.display = pygame.display.set_mode((width, height), flags, vsync)
        pygame.display.set_caption(title)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__app.close()

    def update(self):
        pass

    def render(self):
        self.display.fill((0, 0, 0))
