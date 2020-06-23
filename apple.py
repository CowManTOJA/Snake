from game_object import GameObject
from random import randint
from settings import default_settings


class Apple(GameObject):
    def __init__(self, img, screen):
        self.x = None
        self.y = None

        self.create_apple()

        super().__init__(self.x, self.y, img, screen)

    def create_apple(self):
        self.x = (randint(1, (default_settings['width'] // 25)) * 25) - 25
        self.y = (randint(1, (default_settings['height'] // 25)) * 25) - 25

    def eat(self):
        self.create_apple()
