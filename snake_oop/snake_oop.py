import pygame
import time
import random


class App:
    blue = (0, 0, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)
    snake_block = 20
    snake_speed = 5

    def __init__(self):
        self.running = True
        self.game_over = False
        self.screen = None
        self.font = None
        self.size = self.screen_width, self.screen_height = 800, 600
        self.x = 0
        self.y = 0
        self.x_change = 0
        self.y_change = 0
        self.foodx = 0
        self.foody = 0
        self.clock = None
        self.snake_list = None
        self.snake_length = 0

    def on_init(self):
        pygame.init()
        self.font = pygame.font.Font('fireflysung.ttf', 40)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Snake game')
        self.clock = pygame.time.Clock()
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2
        self.x_change = 0
        self.y_change = 0
        self.running = True
        self.game_over = False
        self.next_random_food()
        self.snake_list = []
        self.snake_length = 1
        return True

    def on_restart(self):
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2
        self.x_change = 0
        self.y_change = 0
        self.game_over = False
        self.next_random_food()
        self.snake_list = []
        self.snake_length = 1

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_change = -App.snake_block
                self.y_change = 0
            elif event.key == pygame.K_RIGHT:
                self.x_change = App.snake_block
                self.y_change = 0
            elif event.key == pygame.K_UP:
                self.y_change = -App.snake_block
                self.x_change = 0
            elif event.key == pygame.K_DOWN:
                self.y_change = App.snake_block
                self.x_change = 0
            if self.game_over:
                if event.key == pygame.K_q:
                    self.running = False
                elif event.key == pygame.K_r:
                    self.game_over = False
                    self.on_restart()

    def on_loop(self):
        if not self.game_over:
            if self.x >= self.screen_width or self.x < 0 or self.y >= self.screen_height or self.y < 0:
                self.game_over = True
            self.x += self.x_change
            self.y += self.y_change
            self.snake_list.append((self.x, self.y))
            if len(self.snake_list) > self.snake_length:
                del self.snake_list[0]
            if self.x == self.foodx and self.y == self.foody:
                print("Yummy!!")
                self.next_random_food()
                self.snake_length += 1

    def on_render(self):
        self.screen.fill(App.white)
        pygame.draw.rect(self.screen, App.red, (self.foodx, self.foody, App.snake_block, App.snake_block))
        self.draw_snake(App.blue, App.green)
        if self.game_over:
            self.message("Game Over!(按Q 結束游戲 或 按R 重新開始)", App.red)
        pygame.display.update()
        self.clock.tick(App.snake_speed)

    def on_cleanup(self):
        pygame.quit()
        quit()

    def on_execute(self):
        if not self.on_init():
            self.running = False

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def message(self, msg, color):
        mesg = self.font.render(msg, True, color)
        self.screen.blit(mesg, (10, self.screen_height // 2))

    def next_random_food(self):
        self.foodx = random.randint(App.snake_block * 5, self.screen_width - App.snake_block * 5) // App.snake_block * App.snake_block
        self.foody = random.randint(App.snake_block * 5, self.screen_height - App.snake_block * 5) // App.snake_block * App.snake_block

    def draw_snake(self, head_color, body_color):
        head = self.snake_list[len(self.snake_list) - 1]
        pygame.draw.rect(self.screen, head_color, (head[0], head[1], App.snake_block, App.snake_block))
        for x in self.snake_list[:-1]:
            pygame.draw.rect(self.screen, body_color, (x[0], x[1], App.snake_block, App.snake_block))


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
