# both pupils point to mouse position with the center at each eye's center position
# So we need to calculate the theta for each eye
import pgzrun
import math

WIDTH = 400
HEIGHT = 400
center=(WIDTH//2,HEIGHT//2)

black = (0,0,0)
white = (255, 255, 255)

eye_radius = 50
pupil_radius = 15
pupil_position = 25

eye_1 = {'x':100 , 'y':200, 'pupil_x':0,'pupil_y':0, 'theta':0}
eye_2 = {'x':300 , 'y':200, 'pupil_x':0,'pupil_y':0, 'theta':0}
speed = 2
def on_mouse_move(pos):
    try:
        eye_1['theta'] = math.atan((pos[1]-eye_1['y'])/(pos[0]-eye_1['x']))
        eye_2['theta'] = math.atan((pos[1]-eye_2['y'])/(pos[0]-eye_2['x']))
        if pos[0]<eye_1['x']:
            eye_1['theta']+=math.pi
        if pos[0]<eye_2['x']:
            eye_2['theta']+=math.pi
    except:
        eye_1['theta']=0
        eye_2['theta']=0
    update_pupil_positions()
def update_pupil_positions():
    eye_1['pupil_x'] = eye_1['x']+pupil_position*math.cos(eye_1['theta'])
    eye_1['pupil_y'] = eye_1['y']+pupil_position*math.sin(eye_1['theta'])
    eye_2['pupil_x'] = eye_2['x']+pupil_position*math.cos(eye_2['theta'])
    eye_2['pupil_y'] = eye_2['y']+pupil_position*math.sin(eye_2['theta'])
def update():
    pass
    
def draw():
    screen.fill(black)
    screen.draw.filled_circle((eye_1['x'],eye_1['y']), eye_radius, color=white)
    screen.draw.filled_circle((eye_2['x'],eye_2['y']), eye_radius, color=white)
    screen.draw.filled_circle((eye_1['pupil_x'],eye_1['pupil_y']), pupil_radius, color=black)
    screen.draw.filled_circle((eye_2['pupil_x'],eye_2['pupil_y']), pupil_radius, color=black)
#clock.schedule_interval(update_theta,1.0)   
pgzrun.go()
