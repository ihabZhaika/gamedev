# Spacewar!
# by KidsCanCode 2015
# For educational purposes only
import pygame
import sys
import random

# define some colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
BGCOLOR = BLACK

TITLE = "War!"
WIDTH = 1080
HEIGHT = 720
FPS = 60
<<<<<<< HEAD
OFFSETX = WIDTH / 2
OFFSETY = HEIGHT / 2

class Ship(pygame.sprite.Sprite):
=======
OFFSETX = int(WIDTH / 2)
OFFSETY = int(HEIGHT / 2)
PLANET_SIZE = 70


class Ship(pygame.sprite.Sprite):

>>>>>>> a54fb569ebbbfc52ff6627d97752d2eab0616b01
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/playerShip1_red.png").convert()
        self.image = pygame.transform.smoothscale(self.image, (50, 38))
        self.image0 = self.image
        self.rect = self.image.get_rect()
<<<<<<< HEAD
        self.pos = pygame.math.Vector2(200, 200)
        self.vel = pygame.math.Vector2(10, 0)
=======
        self.pos = pygame.math.Vector2(0, 250)
        self.vel = pygame.math.Vector2(3, 0)
>>>>>>> a54fb569ebbbfc52ff6627d97752d2eab0616b01
        self.acc = pygame.math.Vector2(0, 0)
        self.thrust = pygame.math.Vector2(0, 0)
        self.rot = 0
        self.player = True
        self.thrust_power = 0.05
        self.rot_speed = 3
<<<<<<< HEAD
=======
        self.health = 100
>>>>>>> a54fb569ebbbfc52ff6627d97752d2eab0616b01

    def get_key_accel(self):
        self.thrust = pygame.math.Vector2(0, 0)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rot += self.rot_speed
        if keystate[pygame.K_RIGHT]:
            self.rot -= self.rot_speed
        if keystate[pygame.K_UP]:
            self.thrust = pygame.math.Vector2(0, -self.thrust_power)
        # adjust thrust vector to facing dir
        self.thrust = self.thrust.rotate(-self.rot)

    def update(self):
        self.rot = self.rot % 360
        # use key controls
        # TODO: ai controls
        if self.player:
            self.get_key_accel()
        # rotate image
        old_center = self.rect.center
        self.image = pygame.transform.rotozoom(self.image0, self.rot, 1.0)
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        # move the sprite
        self.rect.centerx = self.pos.x + OFFSETX
        self.rect.centery = self.pos.y + OFFSETY

<<<<<<< HEAD
=======
class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        pygame.sprite.Sprite.__init__(self)
        self.ship = ship
        self.rot = ship.rot
        self.image = pygame.Surface([5, 10])
        self.image0 = self.image
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = ship.pos - pygame.math.Vector2(0, 25).rotate(-ship.rot)
        self.vel = ship.vel - pygame.math.Vector2(0, 5).rotate(-ship.rot)
        self.acc = pygame.math.Vector2(0, 0)
        self.thrust = pygame.math.Vector2(0, 0)
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.spawn_time > 5000:
            self.kill()
        # rotate image
        old_center = self.rect.center
        self.image = pygame.transform.rotozoom(self.image0, self.rot, 1.0)
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        self.rect.centerx = self.pos.x + OFFSETX
        self.rect.centery = self.pos.y + OFFSETY
>>>>>>> a54fb569ebbbfc52ff6627d97752d2eab0616b01

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        self.running = True
<<<<<<< HEAD
        self.shake = False
        self.all_sprites = pygame.sprite.Group()
=======
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
>>>>>>> a54fb569ebbbfc52ff6627d97752d2eab0616b01
        self.ship = Ship()
        self.all_sprites.add(self.ship)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()  # check for events
            self.update()  # update the game state
            self.draw()    # draw the next frame

    def quit(self):
        pygame.quit()
        sys.exit()

    def events(self):
        # handle all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
<<<<<<< HEAD

    def update(self):
        if self.shake and pygame.time.get_ticks() - self.shake_time > 50:
            for sprite in self.all_sprites:
                sprite.rect.x -= self.shake_x
                sprite.rect.y -= self.shake_y
            self.shake = False
        for body in self.all_sprites:
            dist = body.pos.length()
            dir = body.pos.normalize()
            a = -20000 * dist**-2
=======
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(self.ship)
                    self.bullets.add(bullet)
                    self.all_sprites.add(bullet)

    def update(self):
        for body in self.all_sprites:
            dist = body.pos.length()
            if dist < PLANET_SIZE:
                body.kill()
                continue
            dir = body.pos.normalize()
            a = -2000 * dist**-2
>>>>>>> a54fb569ebbbfc52ff6627d97752d2eab0616b01
            body.acc = dir * a + body.thrust
            body.vel += body.acc
            body.pos += body.vel
        self.all_sprites.update()
<<<<<<< HEAD


    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        msg = "a: {:.2f},{:.2f}".format(self.ship.acc.x, self.ship.acc.y)
        self.draw_text(msg, 18, 10, 10)
        msg = "v: {:.2f},{:.2f}".format(self.ship.vel.x, self.ship.vel.y)
        self.draw_text(msg, 18, 10, 30)
=======
        hits = pygame.sprite.spritecollide(self.ship, self.bullets, True)
        for hit in hits:
            self.ship.health -= 10

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_planet()
        self.all_sprites.draw(self.screen)
        msg = "H: {}".format(self.ship.health)
        self.draw_text(msg, 18, 10, 10)
>>>>>>> a54fb569ebbbfc52ff6627d97752d2eab0616b01
        # uncommment to show FPS (useful for troubleshooting)
        fps_txt = "{:.2f}".format(self.clock.get_fps())
        self.draw_text(str(fps_txt), 18, WIDTH-50, 10)
        pygame.display.flip()

<<<<<<< HEAD
=======
    def draw_planet(self):
        pygame.draw.circle(self.screen, BLUE, (OFFSETX, OFFSETY), PLANET_SIZE)

>>>>>>> a54fb569ebbbfc52ff6627d97752d2eab0616b01
    def draw_text(self, text, size, x, y):
        # utility function to draw text at a given location
        # TODO: move font matching to beginning of file (don't repeat)
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)

<<<<<<< HEAD
    def screen_shake(self, amount):
        if not self.shake:
            self.shake_x = random.randrange(-amount, amount+1)
            self.shake_y = random.randrange(-amount, amount+1)
            for sprite in self.all_sprites:
                sprite.rect.x += self.shake_x
                sprite.rect.y += self.shake_y
            self.shake = True
            self.shake_time = pygame.time.get_ticks()

=======
>>>>>>> a54fb569ebbbfc52ff6627d97752d2eab0616b01
    def start_screen(self):
        pass

    def go_screen(self):
        pass

g = Game()
while True:
    g.start_screen()
    g.new()
    g.run()
    g.go_screen()