from commons import *


class Ball:
    def __init__(self, location_v, velocity_v):
        self.loc = location_v
        self.vel = velocity_v

    def next_position(self):
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
        fill('#88ED77')
        ellipse(self.loc.x, self.loc.y, BALL_DIAMETER, BALL_DIAMETER)

    def check_collision(self, other_ball):
        # dist = self.location.copy(). d = v1.dist(v2)
        #  v1 =
        d = self.loc.dist(other_ball.loc)
        if d < BALL_DIAMETER:
            loc_diff = self.loc.copy().sub(other_ball.loc)
            vel_diff = self.vel.copy().sub(other_ball.vel)
            self.vel.sub(vel_diff.dot(loc_diff))
        pass
