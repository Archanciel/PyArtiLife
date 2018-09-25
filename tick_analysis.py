
# coding=utf-8

# imports the Pygame library
import pygame


def main():
    # initializes Pygame
    pygame.init()

    # sets the window title
    pygame.display.set_caption(u'Time elapsed since the initialization of Pygame')

    # sets the window size
    pygame.display.set_mode((400, 400))

    # creates a clock
    clock = pygame.time.Clock()

    # is the application running?
    is_running = True

    # if the application is running
    while is_running:
        # limits updates to 5 frames per second (FPS)
        clock.tick(30)

        # gets events from the event queue
        for event in pygame.event.get():
            # if the 'close' button of the window is pressed
            if event.type == pygame.QUIT:
                # stops the application
                is_running = False

        # gets the number of milliseconds elapsed after calling 'pygame.init()'
        ticks = pygame.time.get_ticks()

        # prints on the console the number of milliseconds
        print(ticks)

    # finalizes Pygame
    pygame.quit()


if __name__ == '__main__':
    main()