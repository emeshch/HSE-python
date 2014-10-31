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
        """
        creating tank body as a Rect and defining its colour and barrel angle according to id
        """
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
        """
        rotating the barrel in [0;pi]
        """
        # the angle should be in [0; pi]
        if (self.phi >= 0 and direction == 'ccw') or (self.phi <= math.pi and direction == 'cw'):
            self.phi += DELTA_PHI if direction == 'ccw' else - DELTA_PHI
            if self.phi < 0:
                self.phi = 0
            if self.phi > math.pi:
                self.phi = math.pi

    def display(self):
        """
        drawing the tank and making it move as a unit
        """
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
        """
        tank movement in the game window
        """
        # moving in the window
        if direction == 'right':
            if self.body.right + 10 <= screen_width:
                self.body = self.body.move(10, 0)
        else:
            if self.body.left - 10 >= 0:
                self.body = self.body.move(-10, 0)

        self.display()


class Particle(pygame.sprite.Sprite):
    """
    bullet is a Particle
    it takes the barrel angle from the tank
    we draw it in a display() method and change the coordinates in update()

    """
    def __init__(self, tank_phi, x, y):
        """
        creating a particle with the right parameters
        """
        pygame.sprite.Sprite.__init__(self)
        self.phi = tank_phi
        self.size = 4
        self.x = x
        self.y = y
        self.t = 0

    def display(self):
        """
        drawing the particle
        """
        # print 'bullet', self.x

        # it's a Rect in the left-hand side (self.bullet)
        self.bullet = pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.size)

    def update(self):
        """
        particle moving
        """
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

# group the sprites to update them easily
bullist1 = pygame.sprite.Group()
bullist2 = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#create the tanks
tank1 = Tank(1, pos1)
tank2 = Tank(2, pos2)


def first_move_right():
    """
    first tank moving to the right
    """
    if not tank1.whole_tank.colliderect(tank2.whole_tank):
        tank1.update(direction='right')


def second_move_left():
    """
    second tank moving to the left
    """
    if not tank2.whole_tank.colliderect(tank1.whole_tank):
        tank2.update(direction='left')


def fire(tank):
    """
    tank fires: a bullet is created, then added to the bulletlist and then drawn
    """
    if tank == tank1:
        bul1 = Particle(tank.phi, tank.a1, tank.b1)
        bullist1.add(bul1)
        bul1.display()
    else:
        bul2 = Particle(tank.phi, tank.a1, tank.b1)
        bullist2.add(bul2)
        bul2.display()


def collision():
    """
    collisions detection
    """
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


def score():
    """
    display the score
    """
    text = font.render("score: {} - {}".format(tank1.score, tank2.score), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = screen_width * 7/8
    textpos.top = screen_height * 7/8
    screen.blit(text, textpos)


done = False        # defines when to exit the gameloop
playtime = 0

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
        elif event.type == pygame.KEYDOWN:
            #tank1 controls
            if event.key == K_d:
                first_move_right()
            elif event.key == K_a:
                tank1.update(direction='left')
            elif event.key == K_w:
                tank1.rotate_barrel(direction='ccw')
            elif event.key == K_s:
                tank1.rotate_barrel(direction='cw')
            elif event.key == K_q:
                fire(tank1)

            # tank2 controls
            elif event.key == K_RIGHT:
                tank2.update()
            elif event.key == K_LEFT:
                second_move_left()
            elif event.key == K_DOWN:
                tank2.rotate_barrel(direction='ccw')
            elif event.key == K_UP:
                tank2.rotate_barrel(direction='cw')
            elif event.key == K_SPACE:
                fire(tank2)

    bullist1.update()
    bullist2.update()
    all_sprites_list.update()

    collision()

    # print "score: {} - {}".format(tank1.score, tank2.score)
    all_sprites_list.draw(screen)

    score()

    pygame.display.flip()

    clock.tick(60)
