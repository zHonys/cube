import numpy as np
import copy

colors = [
    '\033[0;31;41m',  # red
    '\033[0;34;44m',  # blue
    '\033[0;37;47m',  # white
    '\033[0;32;42m',  # green
    '\033[0;33;43m',  # orange
    '\033[0;93;103m',  # yellow
    '\033[0m'  # reset
]


class Cube:
    def __init__(self):
        self.sides = [np.full((3, 3), x) for x in range(6)]

    def draw(self):
        sides = copy.deepcopy(self.sides)
        colored = []

        for _ in range(0, 6):
            sides[_] = sides[_].reshape([9])
            colored.append([])
            for __ in sides[_]:
                colored[_].append(f"{colors[__]}  {colors[-1]}")

        colored = np.array(colored).reshape((6, 3, 3))

        for _ in range(0, 6):
            for __ in range(0, 3):
                for ___ in range(0, 3):
                    print(colored[_][__][___], end=" ")
                print("\n")
            print("\n")

    def read(self, seq):
        _ = 0
        while _ < len(seq):
            if seq[_] == "r":
                self.r()
            elif seq[_] == "u":
                self.u()
            elif seq[_] == "l":
                self.l()
            elif seq[_] == "d":
                self.d()
            elif seq[_] == "f":
                self.f()
            elif seq[_] == "b":
                self.b()
            elif seq[_] == "'":
                _ += 1
                if seq[_] == "r":
                    self._r()
                elif seq[_] == "u":
                    self._u()
                elif seq[_] == "l":
                    self._l()
                elif seq[_] == "d":
                    self._d()
                elif seq[_] == "f":
                    self._f()
                elif seq[_] == "b":
                    self._b()
            _ += 1

    def repeat(self, seq):
        sides = copy.deepcopy(self.sides)
        tim = 1
        self.read(seq)
        while not np.array_equal(sides, self.sides):
            self.read(seq)
            tim += 1
        print(tim)

    def r(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[0][_][2] = self.sides[2][_][2]
        for _ in range(0, 3):
            sides[2][_][2] = self.sides[4][_][2]
        for _ in range(0, 3):
            sides[4][_][2] = self.sides[5][_][2]
        for _ in range(0, 3):
            sides[5][_][2] = self.sides[0][_][2]

        self.sides = copy.deepcopy(sides)

        self.rotateClock(sides, 3)

    def u(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[1][0][_] = self.sides[2][0][_]
        for _ in range(0, 3):
            sides[2][0][_] = self.sides[3][0][_]
        for _ in range(0, 3):
            sides[3][0][_] = self.sides[5][2][2 - _]
        for _ in range(0, 3):
            sides[5][2][2 - _] = self.sides[1][0][_]

        self.sides = copy.deepcopy(sides)

        self.rotateClock(sides, 0)

    def l(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[0][_][0] = self.sides[5][_][0]
        for _ in range(0, 3):
            sides[5][_][0] = self.sides[4][_][0]
        for _ in range(0, 3):
            sides[4][_][0] = self.sides[2][_][0]
        for _ in range(0, 3):
            sides[2][_][0] = self.sides[0][_][0]

        self.sides = copy.deepcopy(sides)

        self.rotateClock(sides, 1)

    def d(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[1][2][_] = self.sides[5][0][2 - _]
        for _ in range(0, 3):
            sides[5][0][2 - _] = self.sides[3][2][_]
        for _ in range(0, 3):
            sides[3][2][_] = self.sides[2][2][_]
        for _ in range(0, 3):
            sides[2][2][_] = self.sides[1][2][_]

        self.sides = copy.deepcopy(sides)

        self.rotateClock(sides, 4)

        self.sides = copy.deepcopy(sides)

    def f(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[0][2][_] = self.sides[1][_][2]
        for _ in range(0, 3):
            sides[1][_][2] = self.sides[4][0][_]
        for _ in range(0, 3):
            sides[4][0][_] = self.sides[3][_][0]
        for _ in range(0, 3):
            sides[3][_][0] = self.sides[0][2][_]

        self.sides = copy.deepcopy(sides)

        self.rotateClock(sides, 2)

    def b(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[0][0][_] = self.sides[3][_][2]
        for _ in range(0, 3):
            sides[3][_][2] = self.sides[4][2][2 - _]
        for _ in range(0, 3):
            sides[4][2][_] = self.sides[1][_][0]
        for _ in range(0, 3):
            sides[1][_][0] = self.sides[0][0][2 - _]

        self.sides = copy.deepcopy(sides)

        self.rotateClock(sides, 5)

    def _r(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[0][_][2] = self.sides[5][_][2]
        for _ in range(0, 3):
            sides[5][_][2] = self.sides[4][_][2]
        for _ in range(0, 3):
            sides[4][_][2] = self.sides[2][_][2]
        for _ in range(0, 3):
            sides[2][_][2] = self.sides[0][_][2]

        self.sides = copy.deepcopy(sides)

        self.rotateAntiClock(sides, 3)

    def _u(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[1][0][_] = self.sides[5][2][2 - _]
        for _ in range(0, 3):
            sides[5][2][2 - _] = self.sides[3][0][_]
        for _ in range(0, 3):
            sides[3][0][_] = self.sides[2][0][_]
        for _ in range(0, 3):
            sides[2][0][_] = self.sides[1][0][_]

        self.sides = copy.deepcopy(sides)

        self.rotateAntiClock(sides, 0)

    def _l(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[0][_][0] = self.sides[2][_][0]
        for _ in range(0, 3):
            sides[2][_][0] = self.sides[4][_][0]
        for _ in range(0, 3):
            sides[4][_][0] = self.sides[5][_][0]
        for _ in range(0, 3):
            sides[5][_][0] = self.sides[0][_][0]

        self.sides = copy.deepcopy(sides)

        self.rotateAntiClock(sides, 1)

    def _d(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[1][2][_] = self.sides[2][2][_]
        for _ in range(0, 3):
            sides[2][2][_] = self.sides[3][2][_]
        for _ in range(0, 3):
            sides[3][2][_] = self.sides[5][0][2 - _]
        for _ in range(0, 3):
            sides[5][0][2 - _] = self.sides[1][2][_]

        self.sides = copy.deepcopy(sides)

        self.rotateAntiClock(sides, 4)

    def _f(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[0][2][_] = self.sides[3][_][0]
        for _ in range(0, 3):
            sides[3][_][0] = self.sides[4][0][2 - _]
        for _ in range(0, 3):
            sides[4][0][_] = self.sides[1][_][2]
        for _ in range(0, 3):
            sides[1][_][2] = self.sides[0][2][2 - _]

        self.sides = copy.deepcopy(sides)

        self.rotateAntiClock(sides, 0)

    def _b(self):
        sides = copy.deepcopy(self.sides)

        for _ in range(0, 3):
            sides[0][0][_] = self.sides[1][2 - _][0]
        for _ in range(0, 3):
            sides[1][_][0] = self.sides[4][2][_]
        for _ in range(0, 3):
            sides[4][2][_] = self.sides[3][2 - _][2]
        for _ in range(0, 3):
            sides[3][_][2] = self.sides[0][0][_]

        self.sides = copy.deepcopy(sides)

        self.rotateAntiClock(sides, 5)

    def rotateClock(self, sides, affected_side):
        sides[affected_side] = sides[affected_side].reshape([9])
        self.sides[affected_side] = self.sides[affected_side].reshape([9])

        for _ in range(0, 3):
            sides[affected_side][_ * 2 + 2 + _] = self.sides[affected_side][_]
        for _ in range(0, 3):
            sides[affected_side][(6 - (_ * 4)) + (2 * (_ + 1) + _)] = self.sides[affected_side][2 * (_ + 1) + _]
        for _ in range(0, 3):
            sides[affected_side][((_ * 2 + 2) * -1) + 8 - _] = self.sides[affected_side][8 - _]
        for _ in range(0, 3):
            sides[affected_side][(-6 + (_ * 4)) + (6 - (_ * 3))] = self.sides[affected_side][6 - (_ * 3)]

        sides[affected_side] = sides[affected_side].reshape([3, 3])
        self.sides[affected_side] = self.sides[affected_side].reshape([3, 3])

        self.sides = copy.deepcopy(sides)

    def rotateAntiClock(self, sides, affected_side):
        sides[affected_side] = sides[affected_side].reshape([9])
        self.sides[affected_side] = self.sides[affected_side].reshape([9])

        for _ in range(0, 3):
            sides[affected_side][6 - (_ * 3)] = self.sides[affected_side][_]
        for _ in range(0, 3):
            sides[affected_side][((_ + 1) * 2) + (6 - (_ * 3))] = self.sides[affected_side][6 - (_ * 3)]
        for _ in range(0, 3):
            sides[affected_side][(-6 + (_ * 4)) + 8 - _] = self.sides[affected_side][8 - _]
        for _ in range(0, 3):
            sides[affected_side][(2 * (_ + 1) + _) - (_ + 1) * 2] = self.sides[affected_side][2 * (_ + 1) + _]

        sides[affected_side] = sides[affected_side].reshape([3, 3])
        self.sides[affected_side] = self.sides[affected_side].reshape([3, 3])

        self.sides = copy.deepcopy(sides)


cb = Cube()

cb.read("db")

cb.draw()
