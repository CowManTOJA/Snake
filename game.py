from pygame.locals import *
from game import *
from tkinter import messagebox
import tkinter


def setup_screen():
    screen_res = (default_settings['width'], default_settings['height'])
    screen = pygame.display.set_mode(screen_res)
    pygame.display.set_caption('Snake!')
    pygame.display.set_icon(pygame.image.load(graphics['icon']))

    return screen


def update(screen):
    # Load images
    bg = pygame.image.load(graphics['bg'])

    # Size of picture
    correct_size = (default_settings['cell_width'], default_settings['cell_height'])

    # Load images and check if they have correct size
    tail_img = check_img_size(pygame.image.load(graphics['tail']), correct_size)
    head_img = check_img_size(pygame.image.load(graphics['head']), correct_size)
    apple_img = check_img_size(pygame.image.load(graphics['apple']), correct_size)

    # Create objects
    clock = pygame.time.Clock()
    snake_obj = Snake(0, 0, head_img, screen)
    apple_obj = Apple(0, 0, apple_img, screen)
    apple_obj.create(snake_obj)

    # Main loop
    score = 0
    run = True

    while run:
        pygame.display.set_caption(f'Snake!   Your score: {score}')
        clock.tick(default_settings['FPS'])

        # Events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        # Snake events
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            snake_obj.set_direct('left')
        elif keys[K_RIGHT] or keys[K_d]:
            snake_obj.set_direct('right')
        elif keys[K_UP] or keys[K_w]:
            snake_obj.set_direct('up')
        elif keys[K_DOWN] or keys[K_s]:
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
            score += 1

        snake_obj.move()

        # Set background
        screen.fill((0, 205, 0))
        screen.blit(bg, bg.get_rect())

        # Updates objects
        apple_obj.update()
        snake_obj.update()

        # Refresh
        pygame.display.update()

        if snake_obj.check_death():
            run = False

        # Check if player win
        area = (default_settings['width'] / default_settings['cell_width']) * (
                    default_settings['height'] / default_settings['cell_height'])
        if len(snake_obj) == area:
            root = tkinter.Tk()
            root.withdraw()

            messagebox.showinfo('Good job!', 'You win the game!')


if __name__ == '__main__':
    pygame.init()
    update(setup_screen())
