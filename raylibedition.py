from pyray import *

print("Physics Sim in Python (Raylib Edition)")

def bound_check(position, velocity):
    if position >= 790:
            position = 790
            velocity *= -1
            velocity /= 1.25
    if position <= 10:
        position = 10
        velocity *= -1
        velocity /= 1.25
    return (position, velocity)

velocity_y = 0
velocity_x = 0
velocityset = 0
while velocityset < 2:
    while velocityset == 0:
        try:
            velocity_y = -(float(input("Set the Initial Velocity (Y axis): ")))
            velocityset = 1
        except ValueError:
            print("Try again, choose a number only")
    while velocityset == 1:
        try:
            velocity_x = (float(input("Set the Initial Velocity (X axis): ")))
            velocityset = 2
        except ValueError:
            print("Try again, choose a number only")

init_window(800,800,"PhysicsSim")
set_target_fps(240)
acceleration = 9.8/240
posy = 400
posx = 400

while not window_should_close():

    y_update = bound_check(posy, velocity_y)
    x_update = bound_check(posx, velocity_x)

    posy = y_update[0]
    velocity_y = y_update[1]
    posx = x_update[0]
    velocity_x = x_update[1]
    velocity_y += acceleration
    posy += velocity_y
    velocity_x /= 1.001
    posx += velocity_x
    
    begin_drawing()
    clear_background(WHITE)
    draw_circle(int(posx), int(posy), 10, BLACK)
    end_drawing()
