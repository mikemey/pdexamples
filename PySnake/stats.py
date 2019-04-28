from commons import *


class Stats:

    def __init__(self):
        self.stopped = False
        self.points = 0

    def stop_game(self):
        self.stopped = True

    def next_step(self):
        self.points += 1

    def draw(self):
        fill(COL_TEXT)
        textSize(8)
        text(floor(frameRate), width - 30, 10)

        textSize(14)
        text(self.points, width / 2, 20)

        if self.stopped:
            fill(20, 150)
            rect(0, 0, width, height)
            fill(COL_LOST_TEXT)
            textSize(28)
            text("Game lost.", width / 2 - 60, height / 2)
