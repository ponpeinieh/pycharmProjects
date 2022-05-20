import pygame
pygame.init() #初始化pygame模組
width = 400
height = 300
screen = pygame.display.set_mode((width,height)) #參數形態是tuple

finished = False
blue = (0,0,255) #藍色
while not finished:
    #事件處理迴圈
    for event in pygame.event.get():
        # QUIT 事件
        if event.type == pygame.QUIT:
            finished = True
    # 畫幾何圖形: rect(長方形)
    pygame.draw.rect(screen, blue, pygame.Rect(30,30,60,60),5)
    pygame.display.update() #更新畫面
pygame.quit()
