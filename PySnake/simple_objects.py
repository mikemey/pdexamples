from commons import *


class Background:

    def __init__(self):
        pass

    @staticmethod
    def draw():
        background(COL_BACKGROUND)


class GridPoint(object):

    def __init__(self, pos_v):
        self.pos = pos_v
        self.drawV = draw_vector(pos_v)


class SerpentPart(GridPoint):

    def __init__(self, pos_v):
        super(SerpentPart, self).__init__(pos_v)
        self.textCoord = self.drawV.copy().add(PVector(3, 8))

    def draw(self):
        fill(COL_SERPENT)
        rect(self.drawV.x, self.drawV.y, GRID_WIDTH, GRID_WIDTH, 4)

    def draw_index(self, ix):
        fill(COL_SERPENT_TEXT)
        textSize(8)
        text(ix, self.textCoord.x, self.textCoord.y)

    def offset_copy(self, offset_v):
        return SerpentPart(self.pos.copy().add(offset_v))


class Food(GridPoint):

    def __init__(self, pos_v):
        super(Food, self).__init__(pos_v)
        self.eaten = False

    def respawn(self, pos_v):
        self.__init__(pos_v)

    def eat(self):
        self.eaten = True

    def draw(self):
        fill(COL_FOOD)
        rect(self.drawV.x, self.drawV.y, GRID_WIDTH, GRID_WIDTH, 5)
