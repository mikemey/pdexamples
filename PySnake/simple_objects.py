from commons import *

class Background():

    def draw(self):
        background(COL_BACKGROUND)

class GridPoint(object):

    def __init__(self, posV):
        self.posV = posV
        self.drawV = drawVector(posV)

    def getPos(self):
        return self.posV


class SerpentPart(GridPoint):

    def __init__(self, posV):
        super(SerpentPart, self).__init__(posV)
        self.textCoord = self.drawV.copy().add(PVector(3, 8))

    def draw(self):
        fill(COL_SERPENT)
        rect(self.drawV.x, self.drawV.y, GRID_WIDTH, GRID_WIDTH, 4)

    def drawIndex(self, ix):
        fill(COL_SERPENT_TEXT)
        textSize(8)
        text(ix, self.textCoord.x, self.textCoord.y)

    def offsetCopy(self, offsetV):
        return SerpentPart(self.posV.copy().add(offsetV))

class Food(GridPoint):

    def __init__(self, posV):        
        self.respawn(posV)

    def respawn(self, posV):
        super(Food, self).__init__(posV)
        self.eaten = False

    def eat(self):
        self.eaten = True

    def wasEaten(self):
        return self.eaten

    def draw(self):
        fill(COL_FOOD)
        rect(self.drawV.x, self.drawV.y, GRID_WIDTH, GRID_WIDTH, 5)
