from commons import *
from walls import Walls
from serpent import Serpent
from stats import Stats
from simple_objects import Background, Food


def random_point():
    return PVector(int(random(grid_coord(width))), int(random(grid_coord(height))))


class GameMaster:
    def __init__(self):
        self.walls = None
        self.stats = None
        self.serpent = None
        self.food = None
        self.drawables = None
        self.last_step = None

    def create_game(self):
        self.walls = Walls()
        self.stats = Stats()
        self.serpent = Serpent(START_POSITION, START_LENGTH, self.walls)
        self.food = Food(self.__freePoint__())
        self.drawables = [Background(), self.walls, self.serpent, self.food, self.stats]
        self.last_step = millis()

    def __freePoint__(self):
        while True:
            point = random_point()
            if not self.walls.is_point_in_walls(point) \
                    and not self.serpent.is_point_in_snake(point):
                return point

    def next_frame(self):
        if millis() - self.last_step > STEP_SPEED:
            self.last_step = millis()
            self.__step__()
        for drawable in self.drawables:
            drawable.draw()

    def __step__(self):
        self.serpent.next_step(self.food)
        if self.food.eaten:
            self.food.respawn(self.__freePoint__())
            self.stats.bonus_points(FOOD_BONUS)
        if self.serpent.is_dead():
            noLoop()
            self.stats.stop_game()
        else:
            self.stats.next_step()

    def new_direction(self, new_dir):
        self.serpent.set_direction(new_dir)


gameMaster = GameMaster()


def setup():
    size(int(WORLD_SIZE.x), int(WORLD_SIZE.y))
    noStroke()
    gameMaster.create_game()


def draw():
    gameMaster.next_frame()


def keyPressed():
    if keyCode in (0x26, 0x57):
        gameMaster.new_direction(UP)
    if keyCode in (0x25, 0x41):
        gameMaster.new_direction(LEFT)
    if keyCode in (0x28, 0x53):
        gameMaster.new_direction(DOWN)
    if keyCode in (0x27, 0x44):
        gameMaster.new_direction(RIGHT)
