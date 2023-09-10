import pgzrun
import math

WIDTH = 400
HEIGHT = 400
center = (WIDTH//2, HEIGHT//2) #中心位置

black = (0,0,0)
white = (255, 255, 255)
position_1 = (100, 200)
position_2 = (300, 200)
radius = 50
pupil = 15
theta=0
pupil_position = 25
x=0
y=0
x2=0
y2=0
def on_mouse_move(pos): # pos是一個tuple,儲存了滑鼠的位置(x,y)
    #計算theta
    global theta
    if pos[0]-center[0] !=0:
        theta = math.atan((pos[1]-center[1])/(pos[0]-center[0]))
        if pos[0]<center[0]: #代表滑鼠位置在中心點的左邊
            theta += math.pi #加上180度
        update_pos()
    
def update_pos():
    global theta,x,y,x2,y2
    x = pupil_position*math.cos(theta)
    y = pupil_position*math.sin(theta)
    x2 = pupil_position*math.cos(theta)
    y2 = pupil_position*math.sin(theta)
    
def update():
    pass

def draw():
    screen.fill(black)
    screen.draw.filled_circle(position_1, radius, color=white)
    screen.draw.filled_circle(position_2, radius, color=white)
    screen.draw.filled_circle((position_1[0]+x,position_1[1]+y), pupil, color=black)
    screen.draw.filled_circle((position_2[0]+x2,position_2[1]+y2), pupil, color=black)

pgzrun.go()
