import pygame
import time
import random


def message(screen, font_style, msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, (x, y))


def random_position(screen, snake_block):
    foodx = random.randint(snake_block * 5, screen.get_width() - snake_block * 5) // snake_block * snake_block
    foody = random.randint(snake_block * 5, screen.get_height() - snake_block * 5) // snake_block * snake_block
    return (foodx, foody)


def draw_snake(screen, head_color, body_color, snake_list):
    head = snake_list[len(snake_list) - 1]
    pygame.draw.rect(screen, head_color, head)
    for x in snake_list[:-1]:
        pygame.draw.rect(screen, body_color, x)


def main():
    pygame.init()
    font_style = pygame.font.SysFont(None, 50)
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Snake game')

    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)

    x = screen_width // 2
    y = screen_height // 2

    x_change = 0
    y_change = 0

    snake_block = 20
    snake_speed = 5

    clock = pygame.time.Clock()
    game_over = False

    (foodx, foody) = random_position(screen, snake_block)
    snake_list = []
    snake_length = 1
    score = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0
                elif event.key == pygame.K_a:
                    snake_speed += 5
                    if snake_speed > 60:
                        snake_speed = 60
                elif event.key == pygame.K_s:
                    snake_speed -= 5
                    if snake_speed <= 0:
                        snake_speed = 1
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_over = True

        x += x_change
        y += y_change
        screen.fill(black)
        pygame.draw.rect(screen, red, (foodx, foody, snake_block, snake_block))

        snake_list.append(pygame.Rect(x, y, snake_block, snake_block))
        if len(snake_list) > snake_length:
            del snake_list[0]
        draw_snake(screen, blue, green, snake_list)
        # pygame.draw.rect(screen,blue,pygame.Rect(x,y,snake_block,snake_block))
        if x == foodx and y == foody:
            print("Yummy!!")
            (foodx, foody) = random_position(screen, snake_block)
            score += 1
            snake_length += 1

        message(screen, font_style, f"Score : {score}", green, 50, 50)
        message(screen, font_style, f"Speed : {snake_speed}", yellow, 50, 100)
        pygame.display.update()
        clock.tick(snake_speed)

    message(screen, font_style, "Game over!", red, screen_width // 2, screen_height // 2)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
