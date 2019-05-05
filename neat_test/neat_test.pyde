from nrunner import NRunner
from commons import *

nrunner = NRunner()


def setup():
    size(int(DRAW_SIZE.x), int(DRAW_SIZE.y))
    # noStroke()
    nrunner.setup()


def draw():
    background(COL_BACKGROUND)
    fill(30, 100, 20)
    textSize(10)
    text(floor(frameRate), width - 30, 20)
    nrunner.draw()
    # v1 = PVector(0, 0)
    # v2 = PVector(3, 2)
    # theta = PVector.angleBetween(v1, v2)
    # print('theta: ', theta)
    # print('  deg: ', degrees(theta))
    # noLoop()
