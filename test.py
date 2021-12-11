import numpy

for _ in range(0, 3):
    sides[0][movside][_] = self.sides[l[abs(movside - l[1])][0]][_][abs(l[1] - movside)]
for _ in range(0, 3):
    sides[1][_][movside] = self.sides[l[abs(movside - l[1])][1]][abs(abs(l[1] - 2) - movside)][_]
for _ in range(0, 3):
    sides[4][2 - movside][_] = self.sides[l[abs(movside - l[1])][2]][_][abs(abs(l[1] - 2) - movside)]
for _ in range(0, 3):
    sides[3][_][2 - movside] = self.sides[l[abs(movside - l[1])][3]][abs(l[1] - movside)][_]

print("")

for _ in range(0, 3):
    sides[0][2][_] = self.sides[1][_][2]
for _ in range(0, 3):
    sides[1][_][2] = self.sides[4][0][_]
for _ in range(0, 3):
    sides[4][0][_] = self.sides[3][_][0]
for _ in range(0, 3):
    sides[3][_][0] = self.sides[0][2][_]

for _ in range(0, 3):
    sides[0][0][_] = self.sides[3][_][2]
for _ in range(0, 3):
    sides[3][_][2] = self.sides[4][2][2 - _]
for _ in range(0, 3):
    sides[4][2][_] = self.sides[1][_][0]
for _ in range(0, 3):
    sides[1][_][0] = self.sides[0][0][2 - _]

# reverse

for _ in range(0, 3):
    sides[0][2][_] = self.sides[3][_][0]
for _ in range(0, 3):
    sides[3][_][0] = self.sides[4][0][2 - _]
for _ in range(0, 3):
    sides[4][0][_] = self.sides[1][_][2]
for _ in range(0, 3):
    sides[1][_][2] = self.sides[0][2][2 - _]

for _ in range(0, 3):
    sides[0][0][_] = self.sides[1][2 - _][0]
for _ in range(0, 3):
    sides[1][_][0] = self.sides[4][2][_]
for _ in range(0, 3):
    sides[4][2][_] = self.sides[3][2 - _][2]
for _ in range(0, 3):
    sides[3][_][2] = self.sides[0][0][_]
