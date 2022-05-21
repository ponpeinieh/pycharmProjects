import pygame


def main():
    pygame.init()

    white = (255, 255, 255)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    X = 400
    Y = 300

    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Display text')

    font = pygame.font.SysFont(None, 32)
    text = font.render('Hello World', True, blue, yellow)
    while True:

        # display_surface.fill(white)

        # copying the image surface object
        # to the display surface object at
        # (0, 0) coordinate.
        display_surface.blit(text, (200, 150))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()


if __name__ == "__main__":
    main()
