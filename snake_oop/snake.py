import pygame
import time
import random

def message(screen, font_style, msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen.get_width()/2, screen.get_height()/2])
def random_position(screen, snake_block):
    foodx = random.randint(snake_block*5, screen.get_width()-snake_block*5)//snake_block*snake_block
    foody = random.randint(snake_block*5, screen.get_height()-snake_block*5)//snake_block*snake_block
    return (foodx,foody)
def draw_snake(screen, head_color, body_color, snake_block, snake_list):
    head = snake_list[len(snake_list)-1]
    pygame.draw.rect(screen, head_color , (head[0], head[1], snake_block, snake_block))
    for x in snake_list[:-1]:
        pygame.draw.rect(screen, body_color, (x[0], x[1], snake_block, snake_block))

def main():
    pygame.init() 
    font_style = pygame.font.SysFont(None, 50)
    score_font = pygame.font.SysFont("comicsansms", 35)
    screen_width = 800
    screen_height  = 600
    screen =pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Sname game')
    
    blue=(0,0,255)
    green=(0,255,0)
    red=(255,0,0)
    white = (255, 255, 255)
    
    x1 = screen_width/2
    y1 = screen_height/2
 
    x1_change = 0       
    y1_change = 0

    snake_block=20
    snake_speed = 5

    clock = pygame.time.Clock()
    game_over = False
    
    (foodx,foody) = random_position(screen, snake_block)
    snake_list=[]
    snake_length = 1
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        snake_list.append((x1,y1))
        if len(snake_list) > snake_length:
            del snake_list[0]
        draw_snake(screen, blue, green, snake_block, snake_list)
        #pygame.draw.rect(screen,blue,pygame.Rect(x1,y1,snake_block,snake_block))
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
            (foodx,foody) = random_position(screen, snake_block)
            snake_length += 1
        clock.tick(snake_speed)
        
    message(screen, font_style,"You lost",red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
    
if __name__ == '__main__':
    main()
