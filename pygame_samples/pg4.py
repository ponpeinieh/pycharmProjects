import pygame
pygame.init() #初始化pygame模組
width = 400
height = 300
screen = pygame.display.set_mode((width,height)) #參數形態是tuple

finished = False
blue = (0,0,255) #藍色
red = (255,0,0) #紅色
black = (0,0,0) #黑色(背景)
color = blue
clock = pygame.time.Clock()
x = 30
y = 30
while not finished:
    #事件處理迴圈
    for event in pygame.event.get():
        # QUIT 事件
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = red
            if event.key == pygame.K_UP:
                y-=15
            if event.key == pygame.K_DOWN:
                y+=15
            if event.key == pygame.K_LEFT:
                x-=15
            if event.key == pygame.K_RIGHT:
                x+=15
    # 重新設定主畫面的背景
    screen.fill(black)
    # 畫幾何圖形: rect(長方形)
    pygame.draw.rect(screen, color, pygame.Rect(x,y,60,60),5)
    pygame.display.update() #更新畫面
    #控制一個frame的時間
    clock.tick(60) # 60 frames/sec(60 FPS - frames per second)
pygame.quit()
