import pygame
import time
import random

class App:
    # 定義靜態的常數
    # 例如顔色等
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    snake_block = 10
    

    def __init__(self):
        # 建構子
        # 游戲中可調整的狀態變數做爲物件屬性
        self.running = True
        self.game_over = False
        self.screen = None
        self.font = None
        self.size = self.screen_width, self.screen_height = 800, 600
        self.snake_speed = 0
        self.x = 0
        self.y = 0
        self.x_change = 0
        self.y_change = 0
        self.foodx = 0
        self.foody = 0
        self.clock = None
        self.snake_list = None
        self.score = 0
        self.snake_length = 0

    def on_init(self):
        # 第一次初始化游戲狀態時呼叫
        pygame.init()
        self.font = pygame.font.Font('fireflysung.ttf', 40)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Snake game')
        self.clock = pygame.time.Clock()
        self.snake_speed = 5
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2
        self.x_change = 0
        self.y_change = 0
        self.running = True
        self.game_over = False
        self.next_random_food()
        self.snake_list = []
        self.score = 0
        self.snake_length = 1
        return True

    def on_restart(self):
        #游戲重新開始時呼叫
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2
        self.x_change = 0
        self.y_change = 0
        self.game_over = False
        self.next_random_food()
        self.snake_list = []
        self.score = 0
        self.snake_length = 1

    def on_event(self, event):
        #當觸發某事件時呼叫
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
            elif event.key == pygame.K_a:
                self.snake_speed += 5
                if self.snake_speed > 60:
                    self.snake_speed = 60
            elif event.key == pygame.K_s:
                self.snake_speed -= 5
                if self.snake_speed <= 0:
                    self.snake_speed = 1
            if self.game_over:
                if event.key == pygame.K_q:
                    self.running = False
                elif event.key == pygame.K_r:
                    self.game_over = False
                    self.on_restart()

    def on_loop(self):
        #主要loop 中每個循環呼叫一次, 主要用來更新游戲狀態值
        if not self.game_over:
            self.x += self.x_change
            self.y += self.y_change
            self.snake_list.append(pygame.Rect(self.x, self.y, App.snake_block, App.snake_block))
            if len(self.snake_list) > self.snake_length:
                del self.snake_list[0]
            if self.x == self.foodx and self.y == self.foody:
                # print("Yummy!!")
                self.next_random_food()
                self.snake_length += 1
                self.score += 1
            if self.x >= self.screen_width or self.x < 0 or self.y >= self.screen_height or self.y < 0:
                self.game_over = True
            if self.hit_itself():
                self.game_over = True

    def on_render(self):
        #主要loop 中每個循環呼叫一次, 主要用來更新游戲畫面
        self.screen.fill(App.black)
        pygame.draw.rect(self.screen, App.red, (self.foodx, self.foody, App.snake_block, App.snake_block))
        self.draw_snake(App.blue, App.green)
        self.message(f"Score : {self.score}", App.green, 100, 50)
        self.message(f"Speed : {self.snake_speed}", App.yellow, 100, 100)
        if self.game_over:
            self.message("Game Over!(按Q 結束游戲 或 按R 重新開始)", App.red, self.screen_width // 2, self.screen_height // 2)
        pygame.display.update()
        self.clock.tick(self.snake_speed)

    def on_cleanup(self):
        #游戲結束時呼叫, 釋放資源
        pygame.quit()
        quit()

    def on_execute(self):
        #主要架構方法
        if not self.on_init():
            self.running = False

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
    #其他方法
    def message(self, msg, color, x, y):
        mesg = self.font.render(msg, True, color)
        mesg_rect = mesg.get_rect(center=(x, y))
        self.screen.blit(mesg, mesg_rect)

    def next_random_food(self):
        self.foodx = random.randint(App.snake_block * 5,
                                    self.screen_width - App.snake_block * 5) // App.snake_block * App.snake_block
        self.foody = random.randint(App.snake_block * 5,
                                    self.screen_height - App.snake_block * 5) // App.snake_block * App.snake_block

    def draw_snake(self, head_color, body_color):
        head = self.snake_list[len(self.snake_list) - 1]
        pygame.draw.rect(self.screen, head_color, head)
        for x in self.snake_list[:-1]:
            pygame.draw.rect(self.screen, body_color, x)

    def hit_itself(self):
        head = self.snake_list[len(self.snake_list) - 1]
        collide_index = head.collidelist(self.snake_list[:-1])
        # print(collide_index)
        if collide_index >= 0:
            return True
        else:
            return False

# 主要方法
def main():
    theApp = App()
    theApp.on_execute()

if __name__ == '__main__':
    main()
