import pgzrun
import math

WIDTH = 400
HEIGHT = 400

black = (0,0,0)
white = (255, 255, 255)

eye_radius = 50
pupil_radius = 15
pupil_position = 25

eye_1 = {'x':100 , 'y':200, 'pupil_x':0,'pupil_y':0}
eye_2 = {'x':300 , 'y':200, 'pupil_x':0,'pupil_y':0}
theta = 0
speed = 2
def update():
    global theta
    #更新角度theta
    theta = theta + (speed/360)*2*math.pi
    eye_1['pupil_x'] = eye_1['x']+pupil_position*math.cos(theta)
    eye_1['pupil_y'] = eye_1['y']+pupil_position*math.sin(theta)
    eye_2['pupil_x'] = eye_2['x']+pupil_position*math.cos(-1*theta+math.pi)
    eye_2['pupil_y'] = eye_2['y']+pupil_position*math.sin(-1*theta+math.pi)
    

def draw():
    screen.fill(black)
    screen.draw.filled_circle((eye_1['x'],eye_1['y']), eye_radius, color=white)
    screen.draw.filled_circle((eye_2['x'],eye_2['y']), eye_radius, color=white)
    screen.draw.filled_circle((eye_1['pupil_x'],eye_1['pupil_y']), pupil_radius, color=black)
    screen.draw.filled_circle((eye_2['pupil_x'],eye_2['pupil_y']), pupil_radius, color=black)
    
pgzrun.go()
