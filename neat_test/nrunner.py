from commons import *
from ball import Ball


class Collision(object):
    def __init__(self, tx):
        self.past = tx


class NRunner:
    def __init__(self):
        self.close_encounter = False
        self.balls = []
        for i in range(10):
            self.balls.append(self.__create_ball__())
        # self.balls = [
        #     Ball(PVector(130, 100), PVector(2.4, 2.4)),
        #     Ball(PVector(200, 350), PVector(-2.4, -4)),
        #     create_random_ball(),
        #     create_random_ball(),
        #     create_random_ball(),
        #     create_random_ball(),
        #     create_random_ball(),
        #     create_random_ball()
        # ]

    def __create_ball__(self):
        collision = True
        new_ball = None
        while collision:
            collision = False
            new_ball = Ball(PVector(random(WORLD_SIZE.x), random(240)), PVector(random(-3, 3), random(-3, 3)))
            new_ball.next_position()
            for ball in self.balls:
                if ball.is_colliding_with(new_ball):
                    collision = True
                    break
        return new_ball

    def setup(self):
        pass

    def new_direction(self, ix, dir_v):
        self.balls[ix].vel.add(dir_v)

    def draw(self):
        translate(WORLD_START.x, WORLD_START.y)
        fill(COL_WORLD)
        rect(0, 0, WORLD_SIZE.x, WORLD_SIZE.y)
        self.__calc_next_positions__()
        self.__check_collisions__()
        for ball in self.balls:
            ball.draw()

    def __calc_next_positions__(self):
        for ball in self.balls:
            ball.next_position()

    def __check_collisions__(self):
        collisions = self.__find_collisions__()
        while len(collisions) != 0:
            first_collision = max(collisions, key=lambda c: c.past)
            first_collision.resolve()
            collisions = self.__find_collisions__()

    def __find_collisions__(self):
        # for ball_ix in range(len(self.balls)):
        #     for comp_ix in range(ball_ix + 1, len(self.balls)):
        #         b1, b2 = self.balls[ball_ix], self.balls[comp_ix]
        #         b1.check_collision(b2)
        return [Collision(1), Collision(3), Collision(2)]
