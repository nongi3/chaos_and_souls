from pygame import Surface

from interface.bottom_menu import BottomMenu


class Interface:
    def __init__(self):
        self.bottom_menu = BottomMenu()

    def draw(self, screen: Surface):
        self.bottom_menu.draw(screen)
