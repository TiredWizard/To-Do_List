from math import sqrt


class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def dist(self, other):
        return sqrt(((self.x1 - other.x1) ** 2) + ((self.y1 - other.y1) ** 2))
