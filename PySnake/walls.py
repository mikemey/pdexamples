from commons import *

class Walls:

    def __init__(self):
        self.walls = self.__createWalls__()

    def __createWalls__(self):
        maxGridX = gridCoord(width)
        maxGridY = gridCoord(height)
        return [
            Wall(0, 0, maxGridX, 3),
            Wall(0, maxGridY - 1, maxGridX, 1),
            Wall(0, 0, 1, maxGridY),
            Wall(maxGridX - 1, 0, 1, maxGridY),
            Wall(12, 10, 20, 4)
        ]

    def isPointInWalls(self, pointV):
        for wall in self.walls:
            if wall.isPointInWall(pointV):
                return True
        return False

    def draw(self):
        for wall in self.walls:
            wall.draw()

class Wall:

    def __init__(self, x, y, w, h):
        self.posA = PVector(x, y)
        self.posB = self.posA.copy().add(PVector(w, h))
        self.drawStart = PVector(drawCoord(x), drawCoord(y))
        self.drawSize = PVector(drawCoord(w), drawCoord(h))

    def draw(self):
        fill(COL_WALL)
        rect(self.drawStart.x, self.drawStart.y,
             self.drawSize.x, self.drawSize.y)

    def isPointInWall(self, gridV):
        withinX = self.posA.x <= gridV.x and gridV.x < self.posB.x
        withinY = self.posA.y <= gridV.y and gridV.y < self.posB.y
        return withinX and withinY
