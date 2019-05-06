from math import sqrt, atan, cos, tan, ceil, atan2, sin

from commons import *

BALL_SQ_DISTANCE = BALL_DIAMETER * BALL_DIAMETER
ZOOM = 10


def __square_distance__(v1, v2):
    dx, dy = __delta_xy__(v1, v2)
    return dx * dx + dy * dy


def __delta_xy__(v1, v2):
    return v1.x - v2.x, v1.y - v2.y


class Ball:
    def __init__(self, location_v, velocity_v):
        self.loc = location_v
        self.vel = velocity_v

    def next_position(self):
        self.vel.add(GRAVITY)
        self.loc.add(self.vel)
        self.__check_boundaries__()

    def __check_boundaries__(self):
        self.loc.x = self.__direction_bounds__(X_HI_LIMIT, LO_LIMIT, self.loc.x, WALL_BOUNCE, WALL_FRICTION)
        self.loc.y = self.__direction_bounds__(Y_HI_LIMIT, LO_LIMIT, self.loc.y, WALL_FRICTION, WALL_BOUNCE)

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
        # line(self.loc.x, self.loc.y, self.loc.x - ZOOM * self.vel.x, self.loc.y - ZOOM * self.vel.y)
        fill('#88ED77')
        ellipse(self.loc.x, self.loc.y, BALL_DIAMETER, BALL_DIAMETER)

    def is_colliding_with(self, other):
        return __square_distance__(other.loc, self.loc) < BALL_SQ_DISTANCE

    def check_collision(self, other):
        sq_dist = __square_distance__(other.loc, self.loc)
        if sq_dist < BALL_SQ_DISTANCE:
            # keep distance > BALL_DIAMETER
            d1 = abs(sqrt(sq_dist) - BALL_DIAMETER)
            prev_loc = self.loc.copy().sub(self.vel)
            prev_other_loc = other.loc.copy().sub(other.vel)
            prev_sq_dist = __square_distance__(prev_other_loc, prev_loc)
            d0 = abs(sqrt(prev_sq_dist) - BALL_DIAMETER)
            tx = ceil(d1 / (d0 + d1) * 100) / 100

            self.loc.sub(self.vel.copy().mult(tx))
            other.loc.sub(other.vel.copy().mult(tx))

            unit_v = PVector.fromAngle(atan2(other.loc.y - self.loc.y, other.loc.x - self.loc.x))
            self_impulse = unit_v.copy().setMag(self.vel.dot(unit_v))
            unit_v.rotate(PI)
            other_impulse = unit_v.copy().setMag(other.vel.dot(unit_v))
            # unit_v.normalize()

            # dx, dy = __delta_xy__(other.loc, self.loc)
            # dx, dy = __delta_xy__(self.loc, other.loc)
            # unit_v = PVector(dx, dy)

            # new_self_vel = self.vel.copy().sub(self_impulse).add(other_impulse)
            # new_other_vel = other.vel.copy().sub(other_impulse).add(self_impulse)
            self.vel.sub(self_impulse).add(other_impulse)
            other.vel.sub(other_impulse).add(self_impulse)

            # print('new dist', __square_distance__(other.loc, self.loc))
            # print('unit_v', unit_v)
            # print('unit heading', unit_v.heading())
            # print('------------- SELF ------------------')
            # print('loc', self.loc)
            # print('vel', self.vel)
            # print('vel mag', self.vel.mag())
            # print('imp', self_impulse)
            # print('new vel', new_self_vel)
            # print('new vel mag', new_self_vel.mag())
            # print('------------- OTHER -----------------')
            # print('loc', other.loc)
            # print('vel', other.vel)
            # print('vel mag', other.vel.mag())
            # print('imp', other_impulse)
            # print('new vel', new_other_vel)
            # print('new vel mag', new_other_vel.mag())

            # print('before', self.vel.copy().add(other.vel).mag())
            # self.vel.add(other_impulse)
            # other.vel.add(self_impulse)
            # print(' after', new_self_vel.copy().add(new_other_vel).mag())

            # stroke(24, 92, 200)
            # line(self.loc.x, self.loc.y, self.loc.x + ZOOM * new_self_vel.x, self.loc.y + ZOOM * new_self_vel.y)
            # line(other.loc.x, other.loc.y, other.loc.x + ZOOM * new_other_vel.x, other.loc.y + ZOOM * new_other_vel.y)

            # stroke(0)
            # noLoop()
            # line(self.loc.x, self.loc.y, self.loc.x + ZOOM * other_impulse.x, self.loc.y + ZOOM * other_impulse.y)
            # line(other.loc.x, other.loc.y, other.loc.x + ZOOM * self_impulse.x, other.loc.y + ZOOM * self_impulse.y)
