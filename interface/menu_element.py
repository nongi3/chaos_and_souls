import pygame
from pygame import Surface


class MenuElement:
    def __init__(self, pos, name):
        self.__WIDTH = 150
        self.__HEIGHT = 100
        self.__BACKGROUND = pygame.image.load('img/interface/button.png')

        self.pos = pos
        self.name = name

    def get_width(self):
        return self.__WIDTH

    def get_height(self):
        return self.__HEIGHT

    def draw(self, screen: Surface):
        screen.blit(self.__BACKGROUND, self.pos)
