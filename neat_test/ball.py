from math import sqrt, atan, cos, tan

from commons import *

BALL_SQ_DISTANCE = BALL_DIAMETER * BALL_DIAMETER
ZOOM = 50


class Ball:
    def __init__(self, location_v, velocity_v):
        self.loc = location_v
        self.vel = velocity_v

    def next_position(self):
        # self.vel.add(GRAVITY)
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
        # fill('#88ED77')
        point(self.loc.x, self.loc.y)
        stroke(300, 155, 50)
        line(self.loc.x, self.loc.y, self.loc.x - ZOOM * self.vel.x, self.loc.y - ZOOM * self.vel.y)
        noFill()
        ellipse(self.loc.x, self.loc.y, BALL_DIAMETER, BALL_DIAMETER)

    def check_collision(self, other):
        loc_dx = other.loc.x - self.loc.x
        loc_dy = other.loc.y - self.loc.y
        sq_dist = loc_dx * loc_dx + loc_dy * loc_dy
        if sq_dist < BALL_SQ_DISTANCE:
            stroke(150, 40, 40)
            line(self.loc.x, self.loc.y, other.loc.x, other.loc.y)
            theta = atan(loc_dy / loc_dx)
            # line(other.loc.x, other.loc.y, other.loc.x + ZOOM * self_impulse.x, other.loc.y + ZOOM * self_impulse.y)
            # line(other.loc.x, other.loc.y, other.loc.x - ZOOM * other_impulse.x, other.loc.y - ZOOM * other_impulse.y)

            a = BALL_DIAMETER
            c = sqrt(sq_dist)
            g12 = a - c

            alpha = HALF_PI - other.vel.heading() + theta
            beta = self.vel.heading() - theta

            tan_alpha_beta = tan(alpha) / tan(beta)
            b_v = g12 / cos(beta) * (1 - 1 / (1 + tan_alpha_beta))
            self_loc_diff = self.vel.copy().setMag(b_v)

            tan_beta_alpha = 1 / tan_alpha_beta
            d_v = g12 / cos(alpha) * (1 - 1 / (1 + tan_beta_alpha))
            other_loc_diff = other.vel.copy().rotate(PI).setMag(d_v)

            new_self_loc = self.loc.copy().add(self_loc_diff)
            new_other_loc = other.loc.copy().add(other_loc_diff)
            stroke(0)
            line(self.loc.x, self.loc.y, self.loc.x + ZOOM * self_loc_diff.x, self.loc.y + ZOOM * self_loc_diff.y)
            line(other.loc.x, other.loc.y, other.loc.x + ZOOM * other_loc_diff.x, other.loc.y + ZOOM * other_loc_diff.y)

            impulse_v = PVector.fromAngle(theta)
            self_impulse = impulse_v.copy().setMag(self.vel.dot(impulse_v))
            other_impulse = impulse_v.copy().setMag(other.vel.dot(impulse_v))
            new_self_vel = self.vel.copy().add(other_impulse)
            new_other_vel = other.vel.copy().add(self_impulse)

            # f_x = other.loc.x - ZOOM * other.vel.x
            # f_y = other.loc.y - ZOOM * other.vel.y
            # line(f_x, f_y, f_x + ZOOM * new_other_vel.x, f_y + ZOOM * new_other_vel.y)
            #
            stroke(150, 140, 40)
            line(self.loc.x, self.loc.y, self.loc.x + ZOOM * new_self_vel.x, self.loc.y + ZOOM * new_self_vel.y)
            line(other.loc.x, other.loc.y, other.loc.x + ZOOM * new_other_vel.x, other.loc.y + ZOOM * new_other_vel.y)
            print('BALL_SQ_DISTANCE', BALL_SQ_DISTANCE)
            print('sq_dist', sq_dist)
            print('theta', degrees(theta))
            print('alpha', degrees(alpha))
            print('beta', degrees(beta))
            print('self.loc', self.loc)
            print('self_new_loc', new_self_loc)
            print('other.loc', other.loc)
            print('other_new_loc', new_other_loc)
            print('new dist', new_self_loc.dist(new_other_loc))
            # print('self loc', self.loc)
            # print('    self vel', self.vel)
            # print('    self imp', self_impulse)
            # print('new self vel', new_self_vel)
            # print('    oth vel', other.vel)
            # print('    oth imp', other_impulse)
            # print('new oth vel', new_other_vel)
            #
            noLoop()
            # self.loc = new_self_loc
            # self.vel = new_self_vel
            # other.loc = new_other_loc
            # other.vel = new_other_vel
