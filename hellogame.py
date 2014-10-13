import math
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30  # frames per second setting
clock = pygame.time.Clock()

# window size, name, fonts that will be used
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Tanks')
font = pygame.font.Font(None, 36)

#consts with the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# scene and tank parameters
ground_level = screen_height * 3/4
barrel_length = 50
pos1 = 50  #x coordinate
pos2 = 250
phi1 = math.pi/6  #initial barrel angle
phi2 = math.pi - phi1
DELTA_PHI = math.pi/18


class Tank(pygame.sprite.Sprite):  # Sprites are cool in Pygame
    """
    Class for manipulating tanks

    A Tank object consists of a body and a barrel. Body is a rectangle and barrel is a line from (a0, b0) to (a1, b1)
    We draw it using the display() method
    Its barrel rotates either clockwise or counter-clockwise
    When its bullet hits another tank its score ++
    Tank is being moved in update() method

    """
    def __init__(self, tank_id, pos):
        pygame.sprite.Sprite.__init__(self)
        self.body = pygame.Rect(pos, ground_level-30, 80, 30)   # Rects are simple to work with
        self.tank_id = tank_id   # 1 or 2
        self.score = 0
        if self.tank_id == 1:
            self.phi = phi1
            self.color = GREEN
        else:
            self.phi = phi2
            self.color = BLUE


    def rotate_barrel(self, direction='ccw'):
        #print self.phi

        # the angle should be in [0; pi]
        if (self.phi >= 0 and direction == 'ccw') or (self.phi <= math.pi and direction == 'cw'):
            self.phi += DELTA_PHI if direction == 'ccw' else - DELTA_PHI
            if self.phi < 0:
                self.phi = 0
            if self.phi > math.pi:
                self.phi = math.pi

    def display(self):
        # computing the points
        self.a0 = self.body.centerx
        self.b0 = self.body.top
        self.a1 = self.body.centerx + barrel_length*math.cos(self.phi)
        self.b1 = self.body.top - barrel_length*math.sin(self.phi)
        self.bx, self.by = int(self.a1), int(self.b1)

        # drawing
        pygame.draw.rect(screen, self.color, self.body)
        barrel = pygame.draw.line(screen, self.color, (self.a0, self.b0), (self.a1, self.b1), 12)

        # tank as a unit (because it should behave as one)
        self.whole_tank = self.body.union(barrel)

    def update(self, direction='right'):
        # print self.body.right

        # moving in the window
        if direction == 'right':
            if self.body.right + 10 <= screen_width:
                self.body = self.body.move(10, 0)
        else:
            if self.body.left - 10 >= 0:
                self.body = self.body.move(-10, 0)


class Particle(pygame.sprite.Sprite):
    """
    bullet is a Particle
    it takes the barrel angle from the tank
    we draw it in a display() method and change the coordinates in update()

    """
    def __init__(self, tank_phi, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.phi = tank_phi
        self.size = 4
        self.x = x
        self.y = y
        self.t = 0

    def display(self):
        # print 'bullet', self.x

        # it's a Rect in the left-hand side (self.bullet)
        self.bullet = pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.size)

    def update(self):
        # self.tank_id = tank_id
        # print 'bullet upd', self.x


        self.t += 1    # time period of its life
        vel = 20        # initial velocity

        # if math.cos(self.phi) > 0:
            # self.bullet.move(10, 0)

        # moving in ~gravity
        self.x += vel*math.cos(self.phi)
        self.y += -vel*math.sin(self.phi) + 2.5*self.t

        # else:
        #     # self.bullet.move(-10, 0)
        #     self.x -= 10

        self.display()

    # def remove(self):
    #     pygame.draw.circle(screen, WHITE, self.x, self.y)

done = False        # defines when to exit the gameloop
playtime = 0

# group the sprites to update them easily
bullist1 = pygame.sprite.Group()
bullist2 = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#create the tanks
tank1 = Tank(1, pos1)
tank2 = Tank(2, pos2)

#gameloop
while not done:
    milliseconds = clock.tick(FPS)      # do not go faster than this framerate
    playtime += milliseconds / 1000.0

    screen.fill(WHITE)      # fill the background with white

    #draw the ground line and the tanks
    pygame.draw.line(screen, BLACK, (0, ground_level), (screen_width, ground_level), 4)
    tank1.display()
    tank2.display()

    #check the events
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            #tank1 controls
            if event.key == K_d:
                if not tank1.whole_tank.colliderect(tank2.whole_tank):
                    tank1.update(direction='right' )
                    tank1.display()
                    print("move_right")

            elif event.key == K_a:
                tank1.update(direction='left')
                tank1.display()
                print("move_left")

            elif event.key == K_w:
               tank1.rotate_barrel(direction='ccw')
               print("head up")

            elif event.key == K_s:
               tank1.rotate_barrel(direction='cw')
               print("head down")

            elif event.key == K_q:
                bul1 = Particle(tank1.phi, tank1.a1, tank1.b1)
                bullist1.add(bul1)
                bul1.display()

            # tank2 controls
            elif event.key == K_RIGHT:
                tank2.update()
                tank2.display()
                print("2 move_right")

            elif event.key == K_LEFT:
                if not tank2.whole_tank.colliderect(tank1.whole_tank):
                    tank2.update(direction='left')
                    tank2.display()
                    print("2 move_left")

            elif event.key == K_DOWN:
                tank2.rotate_barrel(direction='ccw')
                print("2 head up")

            elif event.key == K_UP:
                tank2.rotate_barrel(direction='cw')
                print("2 head down")

            elif event.key == K_SPACE:
                bul2 = Particle(tank2.phi, tank2.a1, tank2.b1)
                bullist2.add(bul2)
                bul2.display()

    bullist1.update()
    bullist2.update()
    # print len(bullist2)
    all_sprites_list.update()

    # collision_list = [i.bullet for i in bullist1] + [i.bullet for i in bullist2]
    # index1 = tank1.whole_tank.collidelist(collision_list)
    #
    # if index1 > -1:
    #     # print index1
    #     if index1 > len(bullist1) - 1:
    #         bullist2.remove(bullist2[index1 - len(bullist1)])
    #     else:
    #         bullist1.remove(bullist1[index1])


    #collisions detection
    for b in bullist1:
        if b.bullet.colliderect(tank2.whole_tank):
            bullist1.remove(b)
            tank1.score += 1
            continue
        if b.bullet.x > screen_width or b.bullet.y < 0 or b.bullet.x < 0 or b.bullet.y > ground_level:
            bullist1.remove(b)

    for b in bullist2:
        if b.bullet.colliderect(tank1.whole_tank):
            bullist2.remove(b)
            tank2.score += 1
            continue
        if b.bullet.x > screen_width or b.bullet.y < 0 or b.bullet.x < 0 or b.bullet.y > ground_level:
            bullist2.remove(b)

    # print "score: {} - {}".format(tank1.score, tank2.score)
    all_sprites_list.draw(screen)

    #display the score
    text = font.render("score: {} - {}".format(tank1.score, tank2.score), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = screen_width * 7/8
    textpos.top = screen_height * 7/8
    screen.blit(text, textpos)

    pygame.display.flip()

    clock.tick(60)
