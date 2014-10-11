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
# phi = math.pi/9
pos = 100


class Tank(pygame.sprite.Sprite):
    '''
    class for manipulating tanks
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.body = pygame.Rect(pos, y-30, 80, 30)
        self.phi = math.pi/9
        self.DELTA_PHI = math.pi/12

    def rotate_barrel(self, direction='ccw'):
        print self.phi
        if (self.phi >= 0 and direction == 'ccw') or (self.phi <= math.pi and direction == 'cw'):
        # if 0 <= self.phi <= math.pi:
            self.phi += self.DELTA_PHI if direction == 'ccw' else -self.DELTA_PHI
            if self.phi < 0:
                self.phi = 0
            if self.phi > math.pi:
                self.phi = math.pi

    def display(self):
        self.a0 = self.body.centerx
        self.b0 = self.body.top
        self.a1 = self.body.centerx + l*math.cos(self.phi)
        self.b1 = self.body.top - l*math.sin(self.phi)
        self.bx, self.by = int(self.a1), int(self.b1)

        pygame.draw.rect(screen, GREEN, self.body)
        pygame.draw.line(screen, GREEN, (self.a0, self.b0), (self.a1, self.b1), 12)

    def update(self, direction='right'):
        self.body = self.body.move(10 if direction == 'right' else -10, 0)



class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = int(x)
        self.y = int(y)
        self.size = 4

    def display(self):
        print 'bullet', self.x
        self.bullet = pygame.draw.circle(screen, BLACK, (self.x, self.y), self.size)
        # self.bullet = bullet.get_rect()

    # def move(self):
    #
    #     #while self.x < screen_width and self.y < y:
    #         self.x += 10
    #         self.y -= 10
    def update(self):
        print 'bullet upd', self.x
        self.bullet.x += 10
        self.x += 10
        self.display()

    def remove(self):
        pygame.draw.circle(screen, WHITE, self.x, self.y)

done = False
playtime = 0
# bullist = []
bullist = pygame.sprite.Group()
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
                    tank.update()
                    tank.display()
                    print("move_right")

            elif event.key == K_a:
                    tank.update(direction='left')
                    tank.display()
                    print("move_left")

            elif event.key == K_w:
               tank.rotate_barrel(direction='ccw')
               print("head up")

            elif event.key == K_x:
               tank.rotate_barrel(direction='cw')
               print("head down")

            elif event.key == K_s:
                bul = Particle(tank.a1, tank.b1)
                bullist.add(bul)
                bul.display()
    bullist.update()


    all_sprites_list.update()

    # for bul in bullist:
    #     bul.move()
    #     if bul.x > screen_width or bul.y < 0:
    #         bullist.remove(bul)
    for b in bullist:
        if b.x > screen_width or b.y < 0 or b.x < 0 or b.y > y:
            bullist.remove(b)


    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)
