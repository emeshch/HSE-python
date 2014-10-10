import math
import pygame, sys
from pygame.locals import *

pygame.init()
#print('hello')
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
l = 50
phi = math.pi/9
keys = [False, False, False]

class Particle():
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
    def display(self):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.size)
    def move(self):
        self.x += 10
        
    def remove(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

done = False
playtime = 0
#bx, by = 10, 10
while not done:
    milliseconds = clock.tick(FPS) # do not go faster than this framerate
    playtime += milliseconds / 1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
#            print('bye-bye')
            pygame.quit() #delete
            sys.exit() #delete
        elif event.type == pygame.KEYDOWN:
            if event.key == K_d:
                keys[0] = True
                pos += 10
#                print("step")
            elif event.key == K_w:
                keys[1] = True
                phi += math.pi/12
#                print("head up")
            elif event.key == K_s:
                keys[2] = True
#                print('fire!')
    screen.fill(WHITE)    
    pygame.draw.line(screen, BLACK, (0, y), (screen_width, y), 4)
    tank = pygame.Rect(pos, y-30, 80, 30)
    pygame.draw.rect(screen, RED, tank)
    a0 = tank.centerx
    b0 = tank.top
    a1 = tank.centerx + l*math.cos(phi)
    b1 = tank.top - l*math.sin(phi)
    bx, by = int(a1), int(b1)
    pygame.draw.line(screen, RED, (a0,b0), (a1,b1), 10)
    
    if keys[2] == True:
        bul = Particle((bx,by), 5)
        while bul.x < screen_width and bul.y < y:
            bul.move()
            bul.display()
           # time.sleep(0.02)
            
            
    pygame.display.flip()    
    clock.tick(10)

#pygame.display.update()

