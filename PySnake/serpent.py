from commons import *
from simple_objects import SerpentPart


class Serpent:

    def __init__(self, start, length, walls):
        self.isAlive = True
        self.currentDir = RIGHT
        self.nextDir = RIGHT
        self.walls = walls
        self.parts = []
        for ix in range(length):
            offset_v = LEFT.copy().mult(ix)
            self.parts.append(SerpentPart(start.copy().add(offset_v)))

    def set_direction(self, new_dir):
        sum_v = new_dir.copy().add(self.currentDir)
        if sum_v.x != 0 and sum_v.y != 0:
            self.nextDir = new_dir

    def next_step(self, food):
        self.currentDir = self.nextDir
        next_head = self.parts[0].offsetCopy(self.currentDir)
        if self.__isNotEating__(next_head, food):
            self.parts.pop(len(self.parts) - 1)
        self.__checkCollisions__(next_head.getPos())
        self.parts.insert(0, next_head)

    def __isNotEating__(self, head, food):
        if head.getPos().dist(food.getPos()) == 0:
            food.eat()
            return False
        return True

    def __checkCollisions__(self, headV):
        if self.walls.isPointInWalls(headV) or self.is_point_in_snake(headV):
            self.isAlive = False

    def is_point_in_snake(self, pointV):
        for part in self.parts:
            if part.getPos().dist(pointV) == 0:
                return True
        return False

    def isDead(self):
        return not self.isAlive

    def draw(self):
        ix = 0
        for part in self.parts:
            part.draw()
            part.drawIndex(ix)
            ix += 1
