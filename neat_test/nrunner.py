from commons import *
from ball import Ball


def create_random_ball():
    return Ball(PVector(random(WORLD_SIZE.x), random(50)), PVector(random(-2, 2), random(-2, 2)))


class NRunner:
    def __init__(self):
        self.balls = [create_random_ball() for _ in range(0, 50)]

    def setup(self):
        pass

    def draw(self):
        translate(WORLD_START.x, WORLD_START.y)
        fill(COL_WORLD)
        rect(0, 0, WORLD_SIZE.x, WORLD_SIZE.y)
        for ball in self.balls:
            ball.next_position()

        self.__check_collisions__()
        for ball in self.balls:
            ball.draw()

    def __check_collisions__(self):
        for ball_ix in range(len(self.balls)):
            for comp_ix in range(ball_ix + 1, len(self.balls)):
                self.balls[ball_ix].check_collision(self.balls[comp_ix])
