import pygame
import random
def show_score(screen, score):
    font = pygame.font.SysFont(None, 20)
    text_to_show = font.render(f'Score: {score}', True, (0,0,255), (255,255,0))
    screen.blit(text_to_show, (10, 10))
def get_rand_pos():
    rand_x = random.randint(30,370)
    rand_y = random.randint(30,370)
    return (rand_x,rand_y)
def main():
    pygame.init()  # initialize all pygame modules
    width = 400
    height = 400
    screen = pygame.display.set_mode((width, height))  # a tuple
    blue = (0, 0, 255)  # red, green, blue
    red = (255, 0, 0)
    black =(0, 0, 0)
    finished = False
    clock = pygame.time.Clock()
    move_rect = pygame.Rect(200,200,20,20)
    fruit_rect = pygame.Rect(*get_rand_pos(),20,20)
    score = 0
    while not finished:  # main loop (reset screen)
        for event in pygame.event.get():  # event loop
            # QUIT事件
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_rect.y -= 20
                if event.key == pygame.K_DOWN:
                    move_rect.y += 20
                if event.key == pygame.K_LEFT:
                    move_rect.x -= 20
                if event.key == pygame.K_RIGHT:
                    move_rect.x += 20
        screen.fill(black)
        pygame.draw.rect(screen,blue,move_rect)
        pygame.draw.rect(screen,red,fruit_rect)
        #if move_rect.x == fruit_rect.x and move_rect.y == fruit_rect.y:
        if move_rect.colliderect(fruit_rect):
            score+=1
            fruit_rect = pygame.Rect(*get_rand_pos(), 20, 20)
        show_score(screen,score)
        pygame.display.update()  # refresh screen
        # control the refresh rate
        clock.tick(10)
    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
