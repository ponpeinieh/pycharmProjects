import pygame
pygame.init() #初始化pygame模組
width = 400
height = 300
screen = pygame.display.set_mode((width,height)) #參數形態是tuple

finished = False
blue = (0,0,255) #藍色
red = (255,0,0) #紅色
color = blue
clock = pygame.time.Clock()
while not finished:
    #事件處理迴圈
    for event in pygame.event.get():
        # QUIT 事件
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = red
    # 畫幾何圖形: rect(長方形)
    pygame.draw.rect(screen, color, pygame.Rect(30,30,60,60),5)
    pygame.display.update() #更新畫面
    #控制一個frame的時間
    clock.tick(10) # 60 frames/sec(60 FPS - frames per second)
    print(f'時間間隔:{clock.get_time()}')
pygame.quit()
