import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):  # Initialise Game
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):  # Start new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.tiles = pg.sprite.Group()
        t1 = Tile(192, 384, 64, 64)
        t2 = Tile(256, 320, 64, 64)
        self.all_sprites.add(t1)
        self.tiles.add(t1)
        self.all_sprites.add(t2)
        self.tiles.add(t2)
        self.all_sprites.add(self.player)
        self.run()

    def run(self):  # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):  # Game Loop - Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

    def update(self):  # Game Loop - Update
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.tiles, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0
            self.player.grounded = True

    def draw(self):  # Game Loop - Draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        # Game start screen
        pass

    def show_go_screen(self):
        # Game over/continue screen
        pass

# Create new "Game"
g = Game()
g.show_start_screen()


while g.running:
    g.new()
    g.show_go_screen()

pg.quit()