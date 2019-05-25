from math import sin, cos

from commons import *


class Orb:
    def __init__(self, angle, orbit_ix, velocity, media):
        self.angle = angle
        self.orbit_ix = orbit_ix
        self.velocity = velocity
        self.loc = PVector()
        self.calc_location()
        self.media = media

    def calc_location(self):
        self.loc.x = ORBITS[self.orbit_ix] * cos(self.angle) - ORB_DIAMETER / 2
        self.loc.y = ORBITS[self.orbit_ix] * sin(self.angle) - ORB_DIAMETER / 2

    def get_image(self):
        return self.media.images.orb()

    def draw(self):
        self.calc_location()
        image(self.get_image(), self.loc.x, self.loc.y)
        self.angle += self.velocity


class Player(object, Orb):
    def __init__(self, media):
        Orb.__init__(self, 0, 0, 0, media)
        self.velocity_ix = 0
        self.health = 3
        self.points = 0
        self.is_in_day = True

    def up(self):
        self.orbit_ix = min(len(ORBITS) - 1, self.orbit_ix + 1)

    def down(self):
        self.orbit_ix = max(0, self.orbit_ix - 1)

    def reverse(self):
        self.velocity_ix = 1 if self.velocity_ix == 0 else 0

    def in_night(self):
        self.is_in_day = False

    def in_day(self):
        self.is_in_day = True

    def get_image(self):
        if self.is_in_day:
            return self.media.images.player_day()
        return self.media.images.player_night()

    def is_close_to(self, orb, distance=COLLISION_DISTANCE):
        return orb.loc.dist(self.loc) < distance

    def orb_hit(self):
        if self.is_in_day:
            self.points += 1
            self.media.sounds.hit_at_day()
        else:
            self.health -= 1
            self.media.sounds.hit_at_night()
        return self.is_in_day

    def draw(self):
        self.velocity = PLAYER_VELOCITY[self.velocity_ix]
        super(Player, self).draw()
