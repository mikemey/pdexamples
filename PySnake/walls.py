from commons import *


class Walls:

    def __init__(self):
        self.walls = self.__create_walls__()

    @staticmethod
    def __create_walls__():
        max_grid_x = grid_coord(width)
        max_grid_y = grid_coord(height)
        return [
            Wall(0, 0, max_grid_x, 3),
            Wall(0, max_grid_y - 1, max_grid_x, 1),
            Wall(0, 0, 1, max_grid_y),
            Wall(max_grid_x - 1, 0, 1, max_grid_y),
            Wall(12, 10, 20, 4)
        ]

    def is_point_in_walls(self, point_v):
        for wall in self.walls:
            if wall.is_point_in_wall(point_v):
                return True
        return False

    def draw(self):
        for wall in self.walls:
            wall.draw()


class Wall:

    def __init__(self, x, y, w, h):
        self.posA = PVector(x, y)
        self.posB = self.posA.copy().add(PVector(w, h))
        self.drawStart = PVector(draw_coord(x), draw_coord(y))
        self.drawSize = PVector(draw_coord(w), draw_coord(h))

    def draw(self):
        fill(COL_WALL)
        rect(self.drawStart.x, self.drawStart.y,
             self.drawSize.x, self.drawSize.y)

    def is_point_in_wall(self, pos_v):
        within_x = self.posA.x <= pos_v.x < self.posB.x
        within_y = self.posA.y <= pos_v.y < self.posB.y
        return within_x and within_y
