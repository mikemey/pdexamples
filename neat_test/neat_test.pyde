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

def keyPressed():
    if keyCode == 0x57:
        nrunner.new_direction(0, DOWN)
    if keyCode == 0x41:
        nrunner.new_direction(0, RIGHT)
    if keyCode == 0x53:
        nrunner.new_direction(0, UP)
    if keyCode == 0x44:
        nrunner.new_direction(0, LEFT)
    if keyCode == 0x26:
        nrunner.new_direction(1, DOWN)
    if keyCode == 0x25:
        nrunner.new_direction(1, RIGHT)
    if keyCode == 0x28:
        nrunner.new_direction(1, UP)
    if keyCode == 0x27:
        nrunner.new_direction(1, LEFT)
