import math
import pygame, sys
from pygame.locals import *

pygame.init()
print('hello')
FPS = 30 # frames per second setting
clock = pygame.time.Clock()

screen_width = 400
screen_height = 300
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Hello_World')


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pos = 100
y = screen_height *3/4
#tank = pygame.Rect((pos, y-40, 60, 40))
#a0 = tank.centerx
#b0 = tank.top
l = 50 #name it!
phi = math.pi/9
#a1 = tank.centerx + l*math.cos(phi)
#b1 = tank.top - l*math.sin(phi)
keys = [False, False, False]
speed = [2, 2]

class Particle:
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)
    def move(self):
        self.x += 20

done = False
playtime=0
while not done:
    milliseconds = clock.tick(FPS) # do not go faster than this framerate
    playtime += milliseconds / 1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            print('bye-bye')
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_d:
                keys[0] = True
                #print(keys[0])
                pos += 10
                print("step")
            elif event.key == K_w:
                keys[1] = True
                #print(keys[1])
                phi += math.pi/12
                print("up")
            elif event.key == K_s:
                keys[2] = True
                bul = Particle((bx, by), 4)
                bul.display
                bul.move
                print("fire")
                           
    tank = pygame.Rect((pos, y-30, 80, 30))
    a0 = tank.centerx
    b0 = tank.top
    a1 = tank.centerx + l*math.cos(phi)
    b1 = tank.top - l*math.sin(phi)
    bx, by = int(a1), int(b1)
    

    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (0, y), (screen_width, y), 4)
    pygame.draw.rect(screen, RED, tank)
    pygame.draw.line(screen, RED, (a0,b0), (a1,b1), 10)

    
    #pygame.draw.circle(screen, BLUE, (bx,by), 5, 0)
        
    pygame.display.flip()
    clock.tick(10)
    
    


#pygame.display.update()

