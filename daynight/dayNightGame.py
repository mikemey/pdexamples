from math import sin

from commons import *
from media import DayNightMedia
from orbSpawner import OrbSpawner
from orbs import Player


class DayNightGame:
    def __init__(self):
        self.center = PVector(WORLD_SIZE.x / 2, WORLD_SIZE.y / 2)
        self.__media = DayNightMedia()
        self.player = Player(self.__media)
        self.day = Day(self.player)
        self.orbSpawner = OrbSpawner(self.player, self.__media)
        
    def setup(self, load_sound):
        self.__media.setup(load_sound)

    def player_up(self):
        self.player.up()
        self.orbSpawner.has_started = True

    def player_down(self):
        self.player.down()
        self.orbSpawner.has_started = True

    def player_reverse(self):
        self.player.reverse()
        self.orbSpawner.has_started = True

    def draw(self):
        noStroke()
        pushMatrix()
        translate(self.center.x, self.center.y)
        self.day.draw()
        self.player.draw()
        self.orbSpawner.draw()
        popMatrix()
        self.draw_stats()

    def draw_stats(self):
        fill(COL_TEXT_BG)
        rect(0, 0, 120, 120)

        fill(COL_TEXT)
        textSize(10)
        textAlign(0)
        text('Points: ' + str(self.player.points), 30, 20)
        textAlign(1)
        text(' Lives: ' + str(self.player.health), 30, 34)
        textAlign(2)
        text(' Level: ' + str(self.orbSpawner.level()), 30, 48)
        # textAlign(2)
        # text('left-to-spawn: ' + str(self.orbSpawner.__orbs_to_spawn), 30, 62)


class Day:
    def __init__(self, player):
        self.radial_velocity = WORLD_VELOCITY
        self.angle = 0
        self.player = player

    def __next_step__(self):
        if sin(self.player.angle) > 0:
            self.player.in_day()
        else:
            self.player.in_night()
        self.angle += self.radial_velocity
        rotate(self.angle)

    def draw(self):
        self.__next_step__()
        fill(COL_DAY)
        rect(-WORLD_SIZE.x, 0, WORLD_SIZE.x, WORLD_SIZE.y)
        rect(-5, 0, WORLD_SIZE.x, WORLD_SIZE.y)
