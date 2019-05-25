from commons import *


class DayNightMedia:
    def __init__(self):
        self.images = Images()
        self.sounds = Sounds()

    def setup(self, load_sound):
        self.images.setup()
        self.sounds.setup(load_sound)


class Images:
    def __init__(self):
        self.__images = {}

    def setup(self):
        self.__images['orb'] = Images.create_orb(COL_ORB_RGB[0], COL_ORB_RGB[1], COL_ORB_RGB[2])
        self.__images['player-day'] = Images.create_orb(COL_NIGHT, COL_NIGHT, COL_NIGHT)
        self.__images['player-night'] = Images.create_orb(COL_DAY_RGB[0], COL_DAY_RGB[1], COL_DAY_RGB[2])

    @staticmethod
    def create_orb(r, g, b):
        pg = createGraphics(ORB_DIAMETER, ORB_DIAMETER)
        pg.beginDraw()
        pg.background(0, 0, 0, 0)
        pg.fill(r, g, b)
        pg.noStroke()
        pg.ellipse(ORB_DIAMETER / 2, ORB_DIAMETER / 2, ORB_DIAMETER - 1, ORB_DIAMETER - 1)
        pg.filter(BLUR, 0.7)
        pg.endDraw()
        return pg

    def orb(self): return self.__images['orb']

    def player_day(self): return self.__images['player-day']

    def player_night(self): return self.__images['player-night']


class Sounds:
    def __init__(self):
        self.__sounds = {}

    def setup(self, load_sound):
        self.__sounds['hit_day'] = load_sound("day_hit.wav")
        self.__sounds['hit_night'] = load_sound("night_hit.wav")

    def hit_at_day(self): self.__sounds['hit_day'].play()

    def hit_at_night(self): self.__sounds['hit_night'].play()
