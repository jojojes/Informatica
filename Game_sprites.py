# Sprite classes for game
import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.grounded = False

    def update(self):
        self.acc = vec(0, GRAVITY)
        if self.grounded:
            self.acc = vec(0, 0)
        keys = pg.key.get_pressed()

        # Horizontal Movement
        if keys[pg.K_a]:
            if keys[pg.K_LSHIFT]:
                self.acc.x = -PLAYER_ACC * 3
            else:
                self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            if keys[pg.K_LSHIFT]:
                self.acc.x = PLAYER_ACC * 3
            else:
                self.acc.x = PLAYER_ACC
        if keys[pg.K_d] and keys[pg.K_a]:
            self.acc = vec(0, 0)

        # Jumping
        if keys[pg.K_SPACE] and self.grounded is True:
            self.grounded = False
            self.vel.y = -PLAYER_JUMP_STRENGTH

        # Calculate Vector physics
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class Tile(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
