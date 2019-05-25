import random
from math import pi

WORLD_SIZE = PVector(700, 700)

COL_NIGHT = 0
COL_DAY = '#FFFF20'
COL_DAY_RGB = (255, 255, 32)
COL_ORB_RGB = (53, 175, 239)
COL_TEXT = 50
COL_TEXT_BG = 220

WORLD_VELOCITY = 0.01
PLAYER_VELOCITY = (-0.033, 0.02)
ORB_MAX_VELOCITY = 0.030
MIN_VELOCITY_DIFF = 0.002

ORB_DIAMETER = 20
COLLISION_DISTANCE = 15

ORBITS = [100, 150, 200, 250, 300]
ORB_LEVELS = [1, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7]

ORB_SPAWN_SAFE_DISTANCE = 100
ORB_SPAWN_RATE = 0.015


def __random_abs_max(abs_max): return random.uniform(-abs_max, abs_max)


def random_angle(): return __random_abs_max(pi)


def random_orbit(): return random.randint(1, len(ORBITS) - 2)


def random_velocity():
    vel = __random_abs_max(ORB_MAX_VELOCITY)
    while vel - WORLD_VELOCITY < MIN_VELOCITY_DIFF:
        vel = __random_abs_max(ORB_MAX_VELOCITY)
    return vel
