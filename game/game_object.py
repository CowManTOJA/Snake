from abc import ABC
from .settings import *


class GameObject(ABC):
    def __init__(self, x, y, img, screen):
        self.x = x
        self.y = y
        self.width = default_settings['cell_width']
        self.height = default_settings['cell_height']
        self.img = img
        self.screen = screen

    def update(self):
        pos = (self.x, self.y)
        self.screen.blit(self.img, pos)

    def set_position(self, x, y):
        self.x = x
        self.y = y
