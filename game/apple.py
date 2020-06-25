from game.game_object import GameObject
from random import randint
from game.settings import default_settings


class Apple(GameObject):
    def __init__(self, img, screen):
        self.x = None
        self.y = None

        self.create()

        super().__init__(self.x, self.y, img, screen)

    def create(self, snake_obj=None):
        self.x = (randint(1, (default_settings['width'] // 25)) * 25) - 25
        self.y = (randint(1, (default_settings['height'] // 25)) * 25) - 25

        # Check if apple will not be rendered in Snake
        if snake_obj is not None:
            for snake_element in snake_obj.tail:
                if snake_element.x == self.x and snake_element.y == self.y:
                    self.create(snake_obj)
