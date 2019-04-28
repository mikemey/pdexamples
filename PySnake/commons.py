WORLD_SIZE = PVector(600, 500)
START_POSITION = PVector(30, 25)
START_LENGTH = 8
STEP_SPEED = 200

GRID_WIDTH = 10
UP = PVector(0, -1)
DOWN = PVector(0, 1)
LEFT = PVector(-1, 0)
RIGHT = PVector(1, 0)

COL_WALL = '#FF4444'
COL_BACKGROUND = 245
COL_TEXT = '#22BBFF'
COL_LOST_TEXT = '#EE4444'
COL_SERPENT = '#88ED77'
COL_FOOD = '#33FD92'
COL_SERPENT_TEXT = '#EE2277'


def draw_coord(grid_val):
    return grid_val * GRID_WIDTH


def draw_vector(grid_v):
    return grid_v.copy().mult(GRID_WIDTH)


def grid_coord(draw_val):
    return floor(draw_val / GRID_WIDTH)
