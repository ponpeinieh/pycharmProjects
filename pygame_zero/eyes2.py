import pgzrun
import math

WIDTH = 400
HEIGHT = 400

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
def update():
    global theta,x,y,x2,y2
    #更新角度theta
    theta = theta + (2/360)*2*math.pi
    x = pupil_position*math.cos(theta)
    y = pupil_position*math.sin(theta)
    x2 = pupil_position*math.cos(-1*theta+math.pi)
    y2 = pupil_position*math.sin(-1*theta+math.pi)
def draw():
    screen.fill(black)
    screen.draw.filled_circle(position_1, radius, color=white)
    screen.draw.filled_circle(position_2, radius, color=white)
    screen.draw.filled_circle((position_1[0]+x,position_1[1]+y), pupil, color=black)
    screen.draw.filled_circle((position_2[0]+x2,position_2[1]+y2), pupil, color=black)
pgzrun.go()
