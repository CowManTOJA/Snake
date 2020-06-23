import pygame
from pygame.locals import *
from settings import default_settings
from settings import graphics
from snake import Snake
from apple import Apple
from tail import Tail
import sys
import os


def setup():
    # Init
    pygame.init()

    # Screen
    screen_res = (default_settings['width'], default_settings['height'])
    screen = pygame.display.set_mode(screen_res)
    pygame.display.set_caption('Snake by Paweł Niewiarowski')

    return screen


def update(screen):
    # Load images
    try:
        bg = pygame.image.load(graphics['bg'])
        tail_img = pygame.image.load(graphics['tail'])
        head_img = pygame.image.load(graphics['head'])
        apple_img = pygame.image.load(graphics['apple'])
    except pygame.error:
        sys.exit('Where are the graphics?')

    # Create objects
    clock = pygame.time.Clock()
    snake = Snake(0, 0, head_img, screen)
    apple = Apple(apple_img, screen)

    # Main loop
    while default_settings['run']:
        pygame.display.set_caption(f'Snake by Paweł Niewiarowski!   Score: {default_settings["score"]}')
        clock.tick(default_settings['FPS'])

        # Events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                default_settings['run'] = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    default_settings['run'] = False

        # Snake events
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            snake.set_direct('left')
        elif keys[K_RIGHT]:
            snake.set_direct('right')
        elif keys[K_UP]:
            snake.set_direct('up')
        elif keys[K_DOWN]:
            snake.set_direct('down')

        if snake.x == apple.x and snake.y == apple.y:
            apple.eat()

            if not len(snake.tail):
                new_tail = Tail(snake.x, snake.y, tail_img, snake.screen)
            else:
                new_tail = Tail(snake.tail[len(snake.tail) - 1].x, snake.tail[len(snake.tail) - 1].y, tail_img,
                                snake.screen)
            snake.tail.append(new_tail)

            default_settings['score'] += 1

        snake.move()

        if snake.check_death():
            default_settings['run'] = False

        # Set background
        screen.blit(bg, bg.get_rect())

        # Updates objects
        apple.update()
        snake.update_tail()
        snake.update()

        # Refresh
        pygame.display.update()


def main():
    update(setup())


if __name__ == '__main__':
    main()
