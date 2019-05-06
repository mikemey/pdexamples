from math import sqrt, atan, cos, tan

from commons import *

BALL_SQ_DISTANCE = BALL_DIAMETER * BALL_DIAMETER
ZOOM = 100


def __square_distance__(v1, v2):
    dx, dy = __delta_xy__(v1, v2)
    return dx * dx + dy * dy


def __delta_xy__(v1, v2):
    return v1.x - v2.x, v1.y - v2.y


class Ball:
    def __init__(self, location_v, velocity_v):
        self.loc = location_v
        self.vel = velocity_v
        self.highlight = False

    def next_position(self):
        self.highlight = False
        self.vel.add(GRAVITY)
        self.loc.add(self.vel)
        self.__check_boundaries__()

    def __check_boundaries__(self):
        self.loc.x = self.__direction_bounds__(X_HI_LIMIT, LO_LIMIT, self.loc.x, -0.9, 0.95)
        self.loc.y = self.__direction_bounds__(Y_HI_LIMIT, LO_LIMIT, self.loc.y, 0.95, -0.9)

    def __direction_bounds__(self, hi_limit, lo_limit, loc_coord, x_fact, y_fact):
        dist = hi_limit - loc_coord
        if dist < 0:
            self.__update_direction__(x_fact, y_fact)
            return hi_limit
        dist = loc_coord - lo_limit
        if dist < 0:
            self.__update_direction__(x_fact, y_fact)
            return lo_limit
        return loc_coord

    def __update_direction__(self, x_fact, y_fact):
        self.vel.x *= x_fact
        self.vel.y *= y_fact

    def draw(self):
        point(self.loc.x, self.loc.y)
        stroke(300, 155, 50)
        line(self.loc.x, self.loc.y, self.loc.x - ZOOM * self.vel.x, self.loc.y - ZOOM * self.vel.y)
        if self.highlight:
            stroke(60, 155, 50)
            # fill('#88ED77')
        noFill()
        ellipse(self.loc.x, self.loc.y, BALL_DIAMETER, BALL_DIAMETER)

    def check_collision(self, other):
        sq_dist = __square_distance__(other.loc, self.loc)
        if sq_dist < BALL_SQ_DISTANCE:
            self.highlight = True
            other.highlight = True
            d1 = abs(sqrt(sq_dist) - BALL_DIAMETER)
            prev_loc = self.loc.copy().sub(self.vel)
            prev_other_loc = other.loc.copy().sub(other.vel)
            prev_sq_dist = __square_distance__(prev_other_loc, prev_loc)
            d0 = abs(sqrt(prev_sq_dist) - BALL_DIAMETER)
            tx = d1 / (d0 + d1)

            self.loc.sub(self.vel.copy().mult(tx))
            other.loc.sub(other.vel.copy().mult(tx))

            # line(self.loc.x, self.loc.y, other.loc.x, other.loc.y)
            # dx, dy = __delta_xy__(self.loc, other.loc)
            # unit_v = PVector(dy, dx)
            # unit_v.normalize()

            dx, dy = __delta_xy__(other.loc, self.loc)
            unit_v = PVector(dx, dy)
            unit_v.normalize()
            other_impulse = unit_v.copy().setMag(other.vel.copy().dot(unit_v))
            self_impulse = unit_v.copy().setMag(self.vel.copy().dot(unit_v))

            print('before', self.vel.copy().add(other.vel).mag())
            self.vel.add(other_impulse)
            other.vel.add(self_impulse)
            print(' after', self.vel.copy().add(other.vel).mag())

            # stroke(24, 92, 200)
            # line(self.loc.x, self.loc.y, self.loc.x + ZOOM * new_self_vel.x, self.loc.y + ZOOM * new_self_vel.y)
            # line(other.loc.x, other.loc.y, other.loc.x + ZOOM * new_other_vel.x, other.loc.y + ZOOM * new_other_vel.y)

            stroke(0)
            line(other.loc.x, other.loc.y, other.loc.x + ZOOM * self_impulse.x, other.loc.y + ZOOM * self_impulse.y)
            line(self.loc.x, self.loc.y, self.loc.x + ZOOM * other_impulse.x, self.loc.y + ZOOM * other_impulse.y)
            # noLoop()
