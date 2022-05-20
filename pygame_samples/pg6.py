
import pygame

def main():
        pygame.init()

        white = (255, 255, 255)

        X = 400
        Y = 400

        display_surface = pygame.display.set_mode((X, Y ))

        pygame.display.set_caption('Image')

        # create a surface object, image is drawn on it.
        #image = pygame.image.load(r'C:\Users\javat\Pictures\3.png')
        image = pygame.image.load('3.png')

        while True :

                display_surface.fill(white)

                # copying the image surface object
                # to the display surface object at
                # (0, 0) coordinate.
                display_surface.blit(image, (10, 10), area=(50,50,40,40))

                for event in pygame.event.get() :

                        if event.type == pygame.QUIT :

                                pygame.quit()
                                quit()

                pygame.display.update()
			
if __name__ == "__main__":
        main()
