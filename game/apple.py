from game.game_object import GameObject
from random import randint
from game.settings import default_settings


class Apple(GameObject):
    def create(self, snake_obj=None):
        self.x = (randint(1, (default_settings['width'] // default_settings['cell_width'])) * default_settings[
            'cell_width']) - default_settings['cell_width']
        self.y = (randint(1, (default_settings['height'] // default_settings['cell_height'])) * default_settings[
            'cell_height']) - default_settings['cell_height']

        # Check if apple will not be rendered in Snake
        if snake_obj is not None:
            for snake_element in snake_obj.tail:
                if snake_element.x == self.x and snake_element.y == self.y:
                    self.create(snake_obj)
