from typing import List, Any

from pygame import Surface

from interface.menu_element import MenuElement


class BottomMenu:
    buttons: list[MenuElement]

    def __init__(self):
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        self.buttons.append(MenuElement((0, 500), 'Постройки'))

    def draw(self, screen: Surface):
        for button in self.buttons:
            button.draw(screen)
