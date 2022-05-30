from typing import List, Any

from pygame import Surface

from interface.menu_element import MenuElement


class BottomMenu:
    buttons: list[MenuElement]

    def __init__(self):
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        button_pos = 0
        self.buttons.append(MenuElement((button_pos, 500), 'Постройки'))
        button_pos += 160
        self.buttons.append(MenuElement((button_pos, 500), 'Технологии'))
        button_pos += 160
        self.buttons.append(MenuElement((button_pos, 500), 'Фауна'))
        button_pos += 160
        self.buttons.append(MenuElement((button_pos, 500), 'Флора'))
        button_pos += 160
        self.buttons.append(MenuElement((button_pos, 500), 'Задания'))
        button_pos += 160

    def draw(self, screen: Surface):
        for button in self.buttons:
            button.draw(screen)
