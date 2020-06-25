from pygame.locals import *
from game import *
import sys


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
    snake_obj = Snake(0, 0, head_img, screen)
    apple_obj = Apple(apple_img, screen)

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
            snake_obj.set_direct('left')
        elif keys[K_RIGHT]:
            snake_obj.set_direct('right')
        elif keys[K_UP]:
            snake_obj.set_direct('up')
        elif keys[K_DOWN]:
            snake_obj.set_direct('down')

        if snake_obj.x == apple_obj.x and snake_obj.y == apple_obj.y:
            apple_obj.create(snake_obj)

            if not len(snake_obj.tail):
                new_tail = Tail(snake_obj.x, snake_obj.y, tail_img, snake_obj.screen)
            else:
                new_tail = Tail(snake_obj.tail[len(snake_obj.tail) - 1].x,
                                snake_obj.tail[len(snake_obj.tail) - 1].y,
                                tail_img,
                                snake_obj.screen)

            snake_obj.tail.append(new_tail)
            default_settings['score'] += 1

        snake_obj.move()

        if snake_obj.check_death():
            default_settings['run'] = False

        # Set background
        screen.blit(bg, bg.get_rect())

        # Updates objects
        apple_obj.update()
        snake_obj.grow()
        snake_obj.update()

        # Refresh
        pygame.display.update()


def main():
    update(setup())


if __name__ == '__main__':
    main()
