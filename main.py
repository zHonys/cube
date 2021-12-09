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


# sides = [np.full((3, 3), x) for x in range(7)]


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
                #  colored[_].append(f" ")

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
            _ += 1

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

        sides[3] = sides[3].reshape([9])
        self.sides[3] = self.sides[3].reshape([9])

        l = [6, 2, -2]
        for _ in range(0, 3):
            sides[3][_ * 2 + 2 + _] = self.sides[3][_]
        for _ in range(0, 3):
            sides[3][l[_] + (2 * (_ + 1) + _)] = self.sides[3][2 * (_ + 1) + _]
        for _ in range(0, 3):
            sides[3][((_ * 2 + 2) * -1) + 8 - _] = self.sides[3][8 - _]
        for _ in range(0, 3):
            sides[3][(l[_] * -1) + (6 - (_ * 3))] = self.sides[3][6 - (_ * 3)]

        sides[3] = sides[3].reshape([3, 3])
        self.sides[3] = self.sides[3].reshape([3, 3])

        self.sides = copy.deepcopy(sides)

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

        sides[0] = sides[0].reshape([9])
        self.sides[0] = self.sides[0].reshape([9])

        l = [6, 2, -2]
        for _ in range(0, 3):
            sides[0][_ * 2 + 2 + _] = self.sides[0][_]
        for _ in range(0, 3):
            sides[0][l[_] + (2 * (_ + 1) + _)] = self.sides[0][2 * (_ + 1) + _]
        for _ in range(0, 3):
            sides[0][((_ * 2 + 2) * -1) + 8 - _] = self.sides[0][8 - _]
        for _ in range(0, 3):
            sides[0][(l[_] * -1) + (6 - (_ * 3))] = self.sides[0][6 - (_ * 3)]

        sides[0] = sides[0].reshape([3, 3])
        self.sides[0] = self.sides[0].reshape([3, 3])

        self.sides = copy.deepcopy(sides)

    def l(self):
        pass

    def d(self):
        pass

    def f(self):
        pass

    def b(self):
        pass

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

        sides[3] = sides[3].reshape([9])
        self.sides[3] = self.sides[3].reshape([9])

        l = [-6, -2, 2]
        for _ in range(0, 3):
            sides[3][6 - (_ * 3)] = self.sides[3][_]
        for _ in range(0, 3):
            sides[3][((_+1)*2) + (6 - (_ * 3))] = self.sides[3][6 - (_ * 3)]
        for _ in range(0, 3):
            sides[3][l[_] + 8 - _] = self.sides[3][8 - _]
        for _ in range(0, 3):
            sides[3][(2 * (_ + 1) + _) - (_+1)*2] = self.sides[3][2 * (_ + 1) + _]

        sides[3] = sides[3].reshape([3, 3])
        self.sides[3] = self.sides[3].reshape([3, 3])

        self.sides = copy.deepcopy(sides)

    def _u(self):
        pass

    def _l(self):
        pass

    def _d(self):
        pass

    def _f(self):
        pass

    def _b(self):
        pass


cb = Cube()

cb.read("")

cb.draw()
