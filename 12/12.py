inputInstructions = []

with open("12/input.txt", "r") as inputFile:
    for line in inputFile:
        inputInstructions.append([line[:1], int(line[1:])])


shipLocation = [0, 0]
shipDirection = [1, 0]

rightRotation = ((0, 1),
                 (-1, 0))
leftRotation = ((0, -1),
                (1, 0))


def rotate(direction, rotMatrix):
    rotated = []
    for row in rotMatrix:
        rotated.append(row[0]*direction[0] + row[1]*direction[1])
    return rotated


directions = {
    "N": [0, 1],
    "E": [1, 0],
    "S": [0, -1],
    "W": [-1, 0],
    "F": shipDirection,
    "L": leftRotation,
    "R": rightRotation
}

for elem in inputInstructions:
    if elem[0] == "R" or elem[0] == "L":
        for i in range(0, elem[1], 90):
            directions["F"] = rotate(directions["F"], directions[elem[0]])
    elif elem[0] in directions:
        for i, e in enumerate(directions[elem[0]]):
            shipLocation[i] += e*elem[1]

print(shipLocation)
print(abs(shipLocation[0])+abs(shipLocation[1]))
