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


y = screen_height * 3/4
l = 50
phi = math.pi/9
pos = 100


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(pos, y-30, 80, 30)
        self.a0 = self.rect.centerx
        self.b0 = self.rect.top
        self.a1 = self.rect.centerx + l*math.cos(phi)
        self.b1 = self.rect.top - l*math.sin(phi)
        self.bx, self.by = int(self.a1), int(self.b1)

    def display(self):
        pygame.draw.rect(screen, RED, self.rect)
        pygame.draw.line(screen, RED, (self.a0, self.b0), (self.a1, self.b1), 10)

    def update(self):
        # pos += 10
        self.rect.move_ip(10, 0)


class Particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 4

    def display(self):
        pygame.draw.circle(screen, BLACK, self.x, self.y, self.size)

    def move(self):

        #while self.x < screen_width and self.y < y:
            self.x += 10
            self.y -= 10

    def remove(self):
        pygame.draw.circle(screen, WHITE, self.x, self.y)

done = False
playtime = 0
bullist = []
all_sprites_list = pygame.sprite.Group()

tank = Tank()



while not done:
    milliseconds = clock.tick(FPS) # do not go faster than this framerate
    playtime += milliseconds / 1000.0

    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (0, y), (screen_width, y), 4)
    tank.display()

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            pygame.quit()  # delete?
            sys.exit()   # delete?
        elif event.type == pygame.KEYDOWN:
            if event.key == K_d:
                    #tank.move_right()
                    tank.update()
                    tank.display()
                    print("move_right")

            #elif event.key == K_w:
            #    #keys[1] = True
            #    phi += math.pi/12
#           #     print("head up")
            if event.key == K_s:
                bul = Particle(tank.a1, tank.b1)
                bullist.append(bul)
#                print('fire!')

    all_sprites_list.update()

    # for bul in bullist:
    #     bul.move()
    #     if bul.x > screen_width or bul.y < 0:
    #         bullist.remove(bul)



    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)
