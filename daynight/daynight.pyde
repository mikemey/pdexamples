add_library("sound")
from commons import *
from dayNightGame import DayNightGame

dnGame = DayNightGame()


def load_sound(sound_file):
    return SoundFile(this, "sounds/{}".format(sound_file))


def setup():
    size(int(WORLD_SIZE.x), int(WORLD_SIZE.y), P2D)
    noStroke()
    dnGame.setup(load_sound)


def draw():
    background(COL_NIGHT)
    dnGame.draw()
    noFill()
    stroke(189)
    for radius in ORBITS:
        ellipse(WORLD_SIZE.x / 2, WORLD_SIZE.y / 2, radius * 2, radius * 2)


def keyPressed():
    if keyCode == 0x57 or keyCode == 0x26:
        dnGame.player_up()
    if keyCode == 0x53 or keyCode == 0x28:
        dnGame.player_down()
    if keyCode == 0x20:
        dnGame.player_reverse()
