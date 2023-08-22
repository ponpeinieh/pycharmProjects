import pgzrun
import math

WIDTH = 400
HEIGHT = 400

black = (0,0,0)
white = (255, 255, 255)
position_1 = (200, 200)
radius = 50
pupil = 15
theta=0
pupil_position = 25
x=0
y=0
def update():
    global theta,x,y
    #更新角度theta
    theta = theta + (2/360)*2*math.pi
    x = pupil_position*math.cos(theta)
    y = pupil_position*math.sin(theta)
def draw():
    screen.fill(black)
    screen.draw.filled_circle(position_1, radius, color=white)
    screen.draw.filled_circle((position_1[0]+x,position_1[1]+y), pupil, color=black)
pgzrun.go()
