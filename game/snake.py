import pygame
from game.game_object import GameObject
from game.settings import default_settings


class Snake(GameObject):
    def __init__(self, x, y, img, screen):
        super().__init__(x, y, img, screen)
        self.velocity = default_settings['cell_width']
        self.tail = []
        self.direction = {
            'right': True,
            'left': False,
            'up': False,
            'down': False
        }
        self.current_direction = 'right'
        self.last_position = None
        self.rotate = 0

    def move(self):
        self.last_position = (self.x, self.y)
        if self.direction['right']:
            self.x += self.velocity
        elif self.direction['left']:
            self.x -= self.velocity
        elif self.direction['up']:
            self.y -= self.velocity
        elif self.direction['down']:
            self.y += self.velocity

        self.check_border()

    def set_direct(self, direct_to_set):
        if direct_to_set == self.current_direction:
            return
        if direct_to_set == 'right' and self.current_direction == 'left':
            return
        if direct_to_set == 'left' and self.current_direction == 'right':
            return
        if direct_to_set == 'up' and self.current_direction == 'down':
            return
        if direct_to_set == 'down' and self.current_direction == 'up':
            return

        for key in self.direction:
            if key == direct_to_set:
                self.current_direction = key
                self.direction[key] = True
            else:
                self.direction[key] = False

    def check_border(self):
        screen_width = default_settings['width']
        screen_height = default_settings['height']

        if self.x >= screen_width:
            self.x = 0
        elif self.x < 0:
            self.x = screen_width - self.width
        elif self.y < 0:
            self.y = screen_height - self.height
        elif self.y >= screen_height:
            self.y = 0

    def update(self):
        # Update head
        pos = (self.x, self.y)

        if self.current_direction == 'right':
            self.screen.blit(pygame.transform.rotate(self.img, -90), pos)
        elif self.current_direction == 'left':
            self.screen.blit(pygame.transform.rotate(self.img, 90), pos)
        elif self.current_direction == 'up':
            self.screen.blit(pygame.transform.rotate(self.img, 0), pos)
        elif self.current_direction == 'down':
            self.screen.blit(pygame.transform.rotate(self.img, 180), pos)

        # Update tail
        if not self.tail:
            return

        temp = None
        for i in range(1, len(self.tail)):
            if i == 1:
                temp = (self.tail[i].x, self.tail[i].y)
                self.tail[i].set_position(self.tail[i - 1].x, self.tail[i - 1].y)
            else:
                sec_temp = (self.tail[i].x, self.tail[i].y)
                self.tail[i].set_position(temp[0], temp[1])
                temp = sec_temp
            self.tail[i].update()

        self.tail[0].set_position(self.last_position[0], self.last_position[1])
        self.tail[0].update()

    def check_death(self):
        for tail_element in self.tail:
            if tail_element.x == self.x and tail_element.y == self.y:
                return True
