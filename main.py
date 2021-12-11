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
                self.verMov(2)
            elif seq[_] == "u":
                self.horMov(0)
            elif seq[_] == "l":
                self.verMov(0)
            elif seq[_] == "d":
                self.horMov(2)
            elif seq[_] == "f":
                self.sideMov(2)
            elif seq[_] == "b":
                self.sideMov(0)
            elif seq[_] == "'":
                _ += 1
                if seq[_] == "r":
                    self.verMov(2, True)
                elif seq[_] == "u":
                    self.horMov(0, True)
                elif seq[_] == "l":
                    self.verMov(0, True)
                elif seq[_] == "d":
                    self.horMov(2, True)
                elif seq[_] == "f":
                    self.sideMov(2, True)
                elif seq[_] == "b":
                    self.sideMov(0, True)
            _ += 1

    def repeat(self, seq):
        sides = copy.deepcopy(self.sides)
        tim = 1
        self.read(seq)
        while not np.array_equal(sides, self.sides):
            self.read(seq)
            tim += 1
        print(tim)

    def verMov(self, movside, reverse=False):
        sides = copy.deepcopy(self.sides)

        l = [[5, 0, 2, 4], 0, [2, 4, 5, 0]]

        if reverse:
            l[1] = 2

        for _ in range(0, 3):
            sides[0][_][movside] = self.sides[l[abs(movside - l[1])][0]][_][movside]
        for _ in range(0, 3):
            sides[2][_][movside] = self.sides[l[abs(movside - l[1])][1]][_][movside]
        for _ in range(0, 3):
            sides[4][_][movside] = self.sides[l[abs(movside - l[1])][2]][_][movside]
        for _ in range(0, 3):
            sides[5][_][movside] = self.sides[l[abs(movside - l[1])][3]][_][movside]

        self.sides = copy.deepcopy(sides)

        if not reverse:
            self.rotateClock(sides, movside + 1)
        else:
            self.rotateAntiClock(sides, movside + 1)

    def horMov(self, movside, reverse=False):
        sides = copy.deepcopy(self.sides)

        l = [[2, 3, 5, 1], 0, [5, 1, 2, 3]]

        if reverse:
            l[1] = 2

        for _ in range(0, 3):
            sides[1][movside][_] = self.sides[l[abs(movside - l[1])][0]][l[1]][abs(abs(movside - l[1]) - _)]
        for _ in range(0, 3):
            sides[2][movside][_] = self.sides[l[abs(movside - l[1])][1]][movside][_]
        for _ in range(0, 3):
            sides[3][movside][_] = self.sides[l[abs(movside - l[1])][2]][2 - l[1]][abs(abs(2 - movside - l[1]) - _)]
        for _ in range(0, 3):
            sides[5][2 - movside][2 - _] = self.sides[l[abs(movside - l[1])][3]][movside][_]

        self.sides = copy.deepcopy(sides)

        if not reverse:
            self.rotateClock(sides, movside*2)
        else:
            self.rotateAntiClock(sides, movside*2)

    def sideMov(self, movside, reverse=False):
        sides = copy.deepcopy(self.sides)

        l = [[3, 0, 1, 4], 0, [1, 4, 3, 0]]

        if reverse:
            l[1] = 2

        for _ in range(0, 3):
            sides[0][movside][_] = self.sides[l[abs(movside - l[1])][0]][_][abs(l[1] - 2)]
        for _ in range(0, 3):
            sides[1][_][movside] = self.sides[l[abs(movside - l[1])][1]][l[1]][_ - (2 - movside)]
        for _ in range(0, 3):
            sides[4][2 - movside][_] = self.sides[l[abs(movside - l[1])][2]][_][l[1]]
        for _ in range(0, 3):
            sides[3][_][2 - movside] = self.sides[l[abs(movside - l[1])][3]][abs(l[1] - 2)][_ - (2 - movside)]

        self.sides = copy.deepcopy(sides)

        if not reverse:
            self.rotateClock(sides, int((2 - movside)*1.5)+2)
        else:
            self.rotateAntiClock(sides, int((2 - movside)*1.5)+2)

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

cb.repeat("r'u")

cb.draw()
