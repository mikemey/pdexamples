from commons import *
from orbs import Orb


class OrbSpawner:
    def __init__(self, player, media):
        self.player = player
        self.orbs = []
        self.orbs_to_spawn = 0
        self.__level_ix = 0
        self.media = media

    def level(self):
        return self.__level_ix + 1

    def draw(self):
        self.check_collisions()
        self.check_orbs()
        for orb in self.orbs:
            orb.draw()

    def check_collisions(self):
        for orb in list(self.orbs):
            if self.player.is_close_to(orb):
                self.orbs.remove(orb)
                self.player.orb_hit()

    def check_orbs(self):
        if len(self.orbs) == 0 and self.orbs_to_spawn == 0:
            self.orbs_to_spawn = ORB_LEVELS[self.__level_ix]
            self.__level_ix = min(len(ORB_LEVELS) - 1, self.__level_ix + 1)
        if self.orbs_to_spawn > 0 and random.random() < ORB_SPAWN_RATE:
            orb = self.random_orb()
            while self.player.is_close_to(orb, ORB_SPAWN_SAFE_DISTANCE):
                orb = self.random_orb()
            self.orbs.append(orb)
            self.orbs_to_spawn -= 1

    def random_orb(self):
        return Orb(random_angle(), random_orbit(), random_velocity(), self.media)
