import pgzrun
WIDTH = 300
HEIGHT = 300

blue = (0,0,255)
green = (0,255, 0)
red = (255, 0,0)
yellow = (255, 255, 0)

#建立Actor
alien = Actor('alien')
alien.pos = (150,150)

def update():
    alien.left +=1
    if alien.left>WIDTH:
        alien.left= 0

def draw():
    screen.fill(yellow)
    alien.draw()

def on_mouse_down(pos): #pos紀錄滑鼠的位置
    if alien.collidepoint(pos):
        print('被打了!')
    else:
        print('你失手了!')        
    
pgzrun.go()
