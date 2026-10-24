import pygame

print("Physics Sim in Python")

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

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Physics Sim")
clock = pygame.time.Clock()
acceleration = 9.8/240
posy = 400
posx = 400
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    y_update = bound_check(posy, velocity_y)
    x_update = bound_check(posx, velocity_x)

    posy = y_update[0]
    velocity_y = y_update[1]
    posx = x_update[0]
    velocity_x = x_update[1]
    
    screen.fill(pygame.color.Color(255, 255, 255))
    pygame.draw.circle(screen, pygame.color.Color(0, 0, 0), (posx, posy), 10)
    velocity_y += acceleration
    posy += velocity_y
    velocity_x /= 1.001
    posx += velocity_x
    clock.tick(240)
    pygame.display.flip()
pygame.quit()
