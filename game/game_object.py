from abc import ABC


class GameObject(ABC):
    def __init__(self, x, y, img, screen):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.img = img
        self.screen = screen

    def update(self):
        pos = (self.x, self.y)
        self.screen.blit(self.img, pos)

    def set_position(self, x, y):
        self.x = x
        self.y = y
