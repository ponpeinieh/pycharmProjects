import pygame


def main():
    pygame.init()

    white = (255, 255, 255)

    X = 800
    Y = 600

    display_surface = pygame.display.set_mode((X, Y))

    pygame.display.set_caption('Image')

    # create a surface object, image is drawn on it.
    bg_image = pygame.image.load('scene.png').convert()
    icon_image = pygame.image.load('image.png').convert()
    # icon_image.set_alpha(None)
    icon_image.set_colorkey((0, 0, 0))

    while True:

        # display_surface.fill(white)

        # copying the image surface object
        # to the display surface object at
        # (0, 0) coordinate.
        display_surface.blit(bg_image, (0, 0))
        display_surface.blit(icon_image, (450, 350))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()


if __name__ == "__main__":
    main()
