import copy

# Part 1
inputData = []

with open("11/input.txt", "r") as inputFile:
    for line in inputFile:
        inputData.append(list(line.strip()))

originalInput = copy.deepcopy(inputData)
mirrorList = copy.deepcopy(inputData)


coordinates = ((-1, -1), (0, -1), (1, -1), (-1, 0),
               (1, 0), (-1, 1), (0, 1), (1, 1))


def numOfAdjacent(seatMap, x, y):
    adjacentSeats = 0
    for elem in coordinates:
        try:
            if y + elem[1] >= 0 and x + elem[0] >= 0:
                if seatMap[y + elem[1]][x + elem[0]] == "#":
                    adjacentSeats += 1
        except IndexError:
            continue
    return adjacentSeats


def changeSeats(seatMap, adjacentCheck, tolerance):
    stable = True
    for y in range(len(seatMap)):
        for x in range(len(seatMap[0])):
            if seatMap[y][x] == "L" or seatMap[y][x] == "#":
                adjacentSeats = adjacentCheck(seatMap, x, y)
                if seatMap[y][x] == "L" and adjacentSeats == 0:
                    mirrorList[y][x] = "#"
                    stable = False
                elif seatMap[y][x] == "#" and adjacentSeats >= tolerance:
                    mirrorList[y][x] = "L"
                    stable = False
    return stable


while not changeSeats(inputData, numOfAdjacent, 4):
    inputData = copy.deepcopy(mirrorList)


sum = 0
for row in inputData:
    for elem in row:
        if elem == "#":
            sum += 1
print(sum)


# Part 2
inputData = copy.deepcopy(originalInput)
mirrorList = copy.deepcopy(originalInput)

vektors = [list(x) for x in coordinates]
remainingVektors = copy.deepcopy(vektors)


def adjacentDirCheck(seatMap, x, y):
    global remainingVektors
    i = 1
    adjacentSeats = 0
    while remainingVektors:
        found = []
        for elem in remainingVektors:
            try:
                if y + elem[1]*i >= 0 and x + elem[0]*i >= 0:
                    checkingSeat = seatMap[y + elem[1]*i][x + elem[0]*i]
                    if checkingSeat == "#":
                        adjacentSeats += 1
                        found.append(elem)
                    if checkingSeat == "L":
                        found.append(elem)
                else:
                    found.append(elem)
            except IndexError:
                found.append(elem)
        for elem in found:
            remainingVektors.remove(elem)
        i += 1
    remainingVektors = copy.deepcopy(vektors)
    return adjacentSeats


while not changeSeats(inputData, adjacentDirCheck, 5):
    inputData = copy.deepcopy(mirrorList)


sum = 0
for row in inputData:
    for elem in row:
        if elem == "#":
            sum += 1
print(sum)
