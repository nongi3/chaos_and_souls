from typing import Union

import pygame
from pygame import Surface
from pygame.surface import SurfaceType

from interface.interface import Interface


class Game:
    screen: Union[Surface, SurfaceType]

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))

        self.interface = Interface()

    def start(self):
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def draw(self):
        self.interface.draw(self.screen)
        pygame.display.update()


game = Game()
game.start()
