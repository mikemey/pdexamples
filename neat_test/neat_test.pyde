from nrunner import NRunner
from commons import *

nrunner = NRunner()


def setup():
    size(int(DRAW_SIZE.x), int(DRAW_SIZE.y))
    noStroke()
    nrunner.setup()


def draw():
    background(COL_BACKGROUND)
    nrunner.draw()
    # noLoop()
